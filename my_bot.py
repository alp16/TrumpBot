# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:14:47 2020

@author: thors
"""
import tweepy
import time
import random


trump_quotes = ['Stop counting the votes!', 'Vote with smileyCoin!','4 more years!', 'Huuuuge!', 'make smileyCoin great again!', 'the smileyCoin stocks are doing great!']
CONSUMER_KEY =''
CONSUMER_SECRET = ''
ACCESS_KEY =''
ACCESS_SECRET=''
print(help(reversed))

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions=api.mentions_timeline()

for mention in mentions:
    print(str(mention.id)+mention.text)
    ##prentar út alla strengi sem notandi tweetar og taggar bottann
    
FILE_NAME = 'last_seen_id.txt'

def retrive_last_seen_id(file_name):
    f_read = open(file_name,'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


    
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    last_seen_id = retrive_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode = 'extended')
    for mention in reversed(mentions):
        print(str(mention.id)+'-'+mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#trump2020' in mention.full_text.lower():
            ##finnur strengi sem passar við hashtaggið og prentar út ef hann finnur rétta 
            print('found #string')
            print('repsonding')
            api.update_status('@' + random.choice(trump_quotes))
            


##Test
while True:
    reply_to_tweets()
    time.sleep(2)