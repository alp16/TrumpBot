# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:14:47 2020

@author: thors
"""
import tweepy
print('yo')

trump_quotes = ['Stop counting the votes!', 'Vote with smileyCoin!','4 more years!', 'Huuuuge', 'make smileyCoin great again', 'the smileyCoin stocks are doing great']
CONSUMER_KEY =''
CONSUMER_SECRET = ''
ACCESS_KEY =''
ACCESS_SECRET=''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)