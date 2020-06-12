# Load base packages
import pandas as pd
import numpy as np

# Load other key packages
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt

# Machine learning packages
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier

# Twitter API
from TwitterAPI import TwitterAPI
import tweepy
from tweepy import OAuthHandler
from tweepy import API

# Geolocation
import geopandas as gpd

# Streaming
from tweepy.streaming import StreamListener
#from slistener import slistener 

# Other essential packages 
import time
import sys
import json
import csv
import re

"""
INPUTS:
    consumer_key, consumer_secret, access_token, access_token_secret: codes 
    telling twitter that we are authorized to access this data
    hashtag_phrase: the combination of hashtags to search for
OUTPUTS:
    none, simply save the tweet info to a spreadsheet
"""
class SListener(StreamListener):
    def __init__(self, api = None, fprefix = 'streamer'):
        self.api = api or API()
        self.counter = 0
        self.fprefix = fprefix
        self.output  = open('%s_%s.json' % (self.fprefix, time.strftime('%Y%m%d-%H%M%S')), 'w')


# Slistener
class SListener(StreamListener):
    def __init__(self, api = None):
        self.output = open('tweets_%s.json' %
        time.strftime('%Y%m%d-%H%M%S'),'w')
        self.api = api or API()
     
#authObj = json.loads( open('keys.json', 'r').read() )
# Pass API permissions
consumer_key = "rehHagu6gJho85oFtGVQzZpUa"
consumer_secret = "0ShQ8hJzPwSEOYiu0u1QLLD2jHYzJhzwJnyo2wpKyHrwjDPmBG"
access_token = "305201900-4XI5uGsLucYjksazjaJO0h3hdvMKcgKe8mM1A968"
access_token_secret = "gEjlnSo8Tvp1QvuBiHbLW1AClibzrAu4zXR9mQkxfHz3S"
# Pass API permissions
#consumer_key = raw_input('rehHagu6gJho85oFtGVQzZpUa')
#consumer_secret = raw_input('0ShQ8hJzPwSEOYiu0u1QLLD2jHYzJhzwJnyo2wpKyHrwjDPmBG')
#access_token = raw_input('305201900-4XI5uGsLucYjksazjaJO0h3hdvMKcgKe8mM1A968')
#access_token_secret = raw_input('gEjlnSo8Tvp1QvuBiHbLW1AClibzrAu4zXR9mQkxfHz3S')

# Phase 1:  
# Consumer key authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Access key authentication
auth.set_access_token(access_token, access_token_secret)
# Set up the API with the authentication handler
api  = tweepy.API(auth)

# STREAM OPTION 1:
## set up words to track
track = ['Colston', 'Leopold']

listen = SListener(api, 'BLM')
stream = tweepy.Stream(auth, listen)

print("Streaming started...")

stream.filter(track = track)

# STREAM OPTION 2:
# Set up words to track
keywords_to_track = ['#BLM']
# Instantiate the SListener object 
listen = SListener(api)
# Instantiate the Stream object (remove tweepy if code does not run)
stream = tweepy.Stream(auth, listen)
print("Streaming Activated...")
# Begin the collecting data
stream.filter(track = keywords_to_track)


# Phase 2:
authObj = json.loads( open('keys.json', 'r').read())
# Access the JSON file:
import json
# Access the JSON and open them
tweet_json = open('streamer_20200612-094322.json', 'r').read()
# Convert from JSON to Python object
tweet = json.loads(tweet_json)
tweet['text']
tweet['id']


# Access the user data:
# Print user handle
print(tweet['user']['screen_name'])
# Print user follower count
print(tweet['user']['followers_count'])
# Print user location
print(tweet['user']['location'])
# Print user description
print(tweet['user']['description'])

# Acess the retweet data:
# Print the text of the tweet
print(rt['text'])
# Print the text of tweet which has been retweeted
print(rt['retweeted_status']['text'])
# Print the user handle of the tweet
print(rt['user']['screen_name'])
# Print the user handle of the tweet which has been retweeted
print(rt['retweeted_status']['user']['screen_name'])

