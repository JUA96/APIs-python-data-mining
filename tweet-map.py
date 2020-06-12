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
import geopandas as gpd
from tweepy.streaming import StreamListener
import time
import tweepy
from tweepy import OAuthHandler
from tweepy import API
import fiona
import json
import csv
import re


# Pass API permissions
consumer_key = ('rehHagu6gJho85oFtGVQzZpUa')
consumer_secret = ('0ShQ8hJzPwSEOYiu0u1QLLD2jHYzJhzwJnyo2wpKyHrwjDPmBG')
access_token = ('305201900-4XI5uGsLucYjksazjaJO0h3hdvMKcgKe8mM1A968')
access_token_secret = ('gEjlnSo8Tvp1QvuBiHbLW1AClibzrAu4zXR9mQkxfHz3S')

# Create API frame
api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

# Set API to request tweets on response object
response = api.request("statuses/filter", {"track": ["BLM"]}) # filter using keywords attribute
print(response.response)

# Get geographic coordinates
coordinates = []

# Iterate over tweets 
tweets = response.get_iterator()

# Create a while loop to extract set amount of tweets 
count = 0
while count < 50:
    tweet = next(tweets)
    if "place" in tweet and tweet["place"] != None:
        place = tweet["place"]["bounding_box"]["coordinates"][0][0]
        coordinates.append(place)
        count += 1 # increase the counter
        print(place)

# use geopandas to plot by location
from shapely.geometry import shape
world_map = gpd.read_file("worldmap.shp")

# set the plot size
fig, ax = plt.subplots(figsize=(15,15))

# fit the plot 
world_map.plot(ax=ax)

for x, y in coordinates:
    plt.scatter(x,y,marker="o",color="red")
# save the plot figure 
plt.savefig(map.png)
plt.show()
