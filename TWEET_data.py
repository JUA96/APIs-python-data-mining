# Load base packages:
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

from TwitterAPI import TwitterAPI
import geopandas as geopandas
from tweepy.streaming import StreamListener
import time
import tweepy
from tweepy import OAuthHandler
from tweepy import API
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
def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth)
    
    #get the name of the spreadsheet we will write to
    fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))

    #open the spreadsheet we will write to
    with open('%s.csv' % (fname), 'wb') as file:

        w = csv.writer(file)

        #write header row to spreadsheet
        w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count'])

        #for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', \
                                   lang="en", tweet_mode='extended').items(100):
            w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])

# Pass API permissions
consumer_key = ('rehHagu6gJho85oFtGVQzZpUa')
consumer_secret = ('0ShQ8hJzPwSEOYiu0u1QLLD2jHYzJhzwJnyo2wpKyHrwjDPmBG')
access_token = ('305201900-4XI5uGsLucYjksazjaJO0h3hdvMKcgKe8mM1A968')
access_token_secret = ('gEjlnSo8Tvp1QvuBiHbLW1AClibzrAu4zXR9mQkxfHz3S')
# Pass API permissions
#consumer_key = raw_input('rehHagu6gJho85oFtGVQzZpUa')
#consumer_secret = raw_input('0ShQ8hJzPwSEOYiu0u1QLLD2jHYzJhzwJnyo2wpKyHrwjDPmBG')
#access_token = raw_input('305201900-4XI5uGsLucYjksazjaJO0h3hdvMKcgKe8mM1A968')
#access_token_secret = raw_input('gEjlnSo8Tvp1QvuBiHbLW1AClibzrAu4zXR9mQkxfHz3S')
    

# Consumer key authentication
auth = OAuthHandler(consumer_key, consumer_secret)

# Access key authentication
auth.set_access_token(access_token, access_token_secret)

# Set up the API with the authentication handler
api  = API(auth)

class SListener(StreamListener):
    def __init__(self, api = None):
        self.output = open('tweets_%s.json' %
        time.strftime('%Y%m%d-%H%M%S'),'w')
        self.api = api or API()
     
from tweepy.streaming import StreamListener
from tweepy import Stream

# Set up words to track
keywords_to_track = ['#BLM']

# Instantiate the SListener object 
listen = SListener(api)

# Instantiate the Stream object
stream = Stream(auth, listen)
stream.sample()