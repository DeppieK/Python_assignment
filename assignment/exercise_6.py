import re
import tweepy
from tweepy import OAuthHandler
import sys
from datetime import datetime, date, time, timedelta
from tweepy import Cursor

#getting the data from the user
print("Εισαγωγή δεδομένων: ")
access_token = input("access token: ")
access_token_secret = input("access token secret: ")
consumer_key = input("consumer_key: ")
consumer_secret = input("consumer secret: ")

#authenticating...
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#getting the twitter account
user_id = input("Εισαγωγή user ID: ")

statuses = api.user_timeline(user_id, count=10)

all_statuses_text = ''

for status in statuses:
    all_statuses_text += ' ' + status.text

all_statuses_words = all_statuses_text.split()
all_statuses_unique_words = list(set(all_statuses_words))

#sort array ascending by word length
all_statuses_unique_words.sort(key=lambda word: len(word))

print("Top 5 smallest words" , all_statuses_unique_words[:5])
print("Top 5 biggest words" , all_statuses_unique_words[-5:])