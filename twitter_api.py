import tweepy
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Authentication of the account to the twitter api
auth = tweepy.OAuthHandler(api_key, api_key_secret )
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth) #given access to my twitter account

public_tweets = api.home_timeline()
print(public_tweets[0].text)
print(public_tweets[0].created_at)
print(public_tweets[0].user.screen_name)

columns = ['Time', 'User', 'Tweet']
data = []
for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

print(data)

d_frame = pd.DataFrame(data, columns = columns )
print(d_frame)
d_frame.to_csv('tweets.csv')