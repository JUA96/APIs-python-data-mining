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


# Pass API permissions
consumer_key = ('rehHagu6gJho85oFtGVQzZpUa')
consumer_secret = ('0ShQ8hJzPwSEOYiu0u1QLLD2jHYzJhzwJnyo2wpKyHrwjDPmBG')
access_token = ('305201900-4XI5uGsLucYjksazjaJO0h3hdvMKcgKe8mM1A968')
access_token_secret = ('gEjlnSo8Tvp1QvuBiHbLW1AClibzrAu4zXR9mQkxfHz3S')

# Create API frame
api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

# Set API to request tweets on subject
response = api.request("statuses/filter", {"track": ["BLM"]})
print(response.response)

coordinates = []
# Iterate over tweet responses
tweets = response.get_iterator()

count = 0
while count < 50:
    tweet = next(tweets)
    if "place" in tweet and tweet["place"] != None:
        place = tweet["place"]["bounding_box"]["coordinates"][0][0]
        coordinates.append(place)
        count += 1
        print(place)

world_map = gpd.read_file("worldmap.shp")

fig, ax = plt.subplots(figsize=(15,15))

world_map.plot(ax=ax)

for x, y in coordinates:
    plt.scatter(x,y,marker="o",color="red")

plt.savefig(map.png)
plt.show()
