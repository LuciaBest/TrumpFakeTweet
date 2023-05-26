#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 22:12:38 2023

@author: fengluyu
"""

import time
import tweepy

# Replace these values with your own keys
CONSUMER_KEY = "****"
CONSUMER_SECRET = "****"
ACCESS_KEY = "****"
ACCESS_SECRET = "****"


def tweet_line_by_line(file_name):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    # Create API object
    api = tweepy.API(auth)

    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()  # Remove newline characters from end
            if len(line) <= 280:  # Twitter max character count is 280
                try:
                    api.update_status(line)
                    print(f"Tweeted: {line}")
                except tweepy.TweepError as e:
                    print(e.reason)
                time.sleep(60*60*3)  # Sleep for 3 hours
            else:
                print("Line is more than 280 characters, cannot be tweeted")

if __name__ == "__main__":
    tweet_line_by_line('trumpwords.txt')
