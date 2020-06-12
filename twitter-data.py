from textblob import TextBlob
import sys, tweepy
from tweepy.auth import OAuthHandler
from tweepy import API
import matplotlib.pyplot as plt
print("Packages Succesfully Imported")

def percentage(part, whole): 
    return 100 * float(part)/float(whole)

consumerKey = "rehHagu6gJho85oFtGVQzZpUa"
consumerSecret = "0ShQ8hJzPwSEOYiu0u1QLLD2jHYzJhzwJnyo2wpKyHrwjDPmBG"
accessToken = "305201900-4XI5uGsLucYjksazjaJO0h3hdvMKcgKe8mM1A968"
accessTokenSecret = "gEjlnSo8Tvp1QvuBiHbLW1AClibzrAu4zXR9mQkxfHz3S"


auth = OAuthHandler(consumer_key = consumerKey, consumer_secret = consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = API(auth)

searchTerm = input("Enter keyword/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))

tweets = tweepy.Cursor(api.search, q=searchTerm, lang="English").items(noOfSearchTerms)

positive = 0 
negative = 0 
neutral = 0 
polarity = 0

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)