from django.urls import path
from . import views

url_patterns = [
    path('base', views.base, name = 'user-detail-base'),
    path('display', views.display, name= 'user-detail-display'),
    path('home', views.home, name= 'user-detail-home')
]