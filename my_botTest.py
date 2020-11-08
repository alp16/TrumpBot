# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 20:48:29 2020

@author: thors
"""

import tweepy

CONSUMER_KEY ='CXl3P9YWN3gMx7RpGgEzwb1fr'
CONSUMER_SECRET = 'D37KlNwlRiR7PPzLaePEtQFiCCxAkNYSdJCdvAXL6htuctO7G9'
ACCESS_KEY ='1325247044601192448-7BsmRdXKeGI9GXnyjmpa1aE3gst5Wd'
ACCESS_SECRET='gUQQVH4b8hlUjzNyFHmxBIqtpYvi6jXdHJSX2FekCQd04'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions=api.mentions_timeline()


    
    
    
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


last_seen_id = retrive_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
for mention in reversed(mentions):
    print(str(mention.id)+'-'+ mention.full_text)
    last_seen_id = mention.id
    store_last_seen_id(last_seen_id, FILE_NAME)
    if '#helloworld' in mention.full_text.lower():
    ##finnur strengi sem passar við hashtaggið og prentar út ef hann finnur rétta 
        print('found #string')
        print('repsonding')
        api.update_status('@' + mention.user.screen_name +' hello world!',mention.id)
            