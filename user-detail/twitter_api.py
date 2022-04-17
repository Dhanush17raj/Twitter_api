import requests
import json
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAIE3bgEAAAAAsvM3Dy9oyIAlKA898NerVNeBqs0%3DHys7BCtkgOWwDHjqxaWBPt6mNc2RBrQsQPuMsZxd2kvXXphle7'
username='elonmusk'
user_id=44196397
post_id = 1515405264740134918


url= 'https://api.twitter.com/2/users/{}/tweets'.format(user_id)

headers={'Authorization': 'Bearer {}'.format(bearer_token)}

response= requests.request('GET',url,headers=headers)

tweetsData=response.json()
ab = (json.dumps(tweetsData,indent=4,sort_keys=True))


a = "https://api.twitter.com/2/tweets/{}/liking_users".format(post_id)

header={'Authorization': 'Bearer {}'.format(bearer_token)}

respons= requests.request('GET',a,headers=header)

tweets_Data=respons.json()
b = (json.dumps(tweets_Data,indent=4,sort_keys=True))


cd = 'https://api.twitter.com/2/users/:{}/liked_tweets'.format(user_id)

head_ers={'Authorization': 'Bearer {}'.format(bearer_token)}

respo_nse= requests.request('GET',cd,headers=head_ers)

tweetsdata=respo_nse.json()
df = (json.dumps(tweetsdata,indent=4,sort_keys=True))

ret = "https://api.twitter.com/2/tweets/{}/retweeted_by".format(post_id)
Headers={'Authorization': 'Bearer {}'.format(bearer_token)}

Response= requests.request('GET',ret,headers=Headers)

TweetsData=Response.json()
rt = (json.dumps(TweetsData,indent=4,sort_keys=True))

qu = "https://api.twitter.com/2/tweets/{}/quote_tweets".format(post_id)

heaDers={'Authorization': 'Bearer {}'.format(bearer_token)}

REsponse= requests.request('GET',qu,headers=heaDers)

Tweetsdata=REsponse.json()
quo = (json.dumps(Tweetsdata,indent=4,sort_keys=True))



print("Last 10 tweets of the user is", ab)
print("No. of tweets liked by the user:",len(df))
print("No. of likes that a tweet is getting:",len(b))
print("No. of re-tweets a tweet is getting:",len(rt))
print("No. of quote_tweets a tweet is getting:",len(quo))

