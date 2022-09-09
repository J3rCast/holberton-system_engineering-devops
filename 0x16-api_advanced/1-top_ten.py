#!/usr/bin/python3
"""This file contains a function that queries the Reddit API"""


import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts
        listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    r = requests.get(url, headers=headers)
    data = r.json()["data"]["children"]

    for i in data:
        print(i["data"]["title"])

import sys
if len(sys.argv) < 2:
    print("Please pass an argument for the subreddit to search.")
else:
    top_ten(sys.argv[1])
