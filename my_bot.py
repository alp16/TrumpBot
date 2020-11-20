# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:14:47 2020

@author: thors
"""
import tweepy
import time
import random


##TODO
##Followa þann sem taggar okkur í tweeti, annars getum við ekki commentað á tweetið.
##Hugsanlega einhver önnur virkni?


trump_quotes = ['Stop counting the votes!', 'Vote with smileyCoin!','4 more years!', 'Huuuuge!', 'make smileyCoin great again!', 'the smileyCoin stocks are doing great!']
biden_diss = ['sleepy joe!', 'I did more then sleepy joe in 4 years than him in 40 years!','worst candidate ever!']
CONSUMER_KEY ='CXl3P9YWN3gMx7RpGgEzwb1fr'
CONSUMER_SECRET = 'D37KlNwlRiR7PPzLaePEtQFiCCxAkNYSdJCdvAXL6htuctO7G9'
ACCESS_KEY ='1325247044601192448-7BsmRdXKeGI9GXnyjmpa1aE3gst5Wd'
ACCESS_SECRET='gUQQVH4b8hlUjzNyFHmxBIqtpYvi6jXdHJSX2FekCQd04'

print(random.choice(trump_quotes))
print(random.choice(biden_diss))
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


    
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
        if '' in mention.full_text.lower():
            api.create_friendship(mention.user.screen_name)
        if '#helloworld' in mention.full_text.lower():
            ##finnur strengi sem passar við hashtaggið og prentar út ef hann finnur rétta 
            print('found #helloworld')
            print('repsonding')
            api.update_status('@' + mention.user.screen_name +' hello world!',mention.id)
        if '#smileycoin' in mention.full_text.lower():
            print('found #smileycoin')
            print('responding')
            ##fylla út if setning til commenta það sem við viljum
        
            
def follow_latest():
    followers = api.followers()
    print(len(followers))
    for follower in followers:
        print(follower.screen_name)
        api.create_friendship(follower.screen_name)


##Test
while True:
    reply_to_tweets()
    follow_latest()
    time.sleep(30)