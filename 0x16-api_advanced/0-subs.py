#!/usr/bin/python3
"""This file contains a function that queries the Reddit API"""


import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=1".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    r = requests.get(url, headers=headers)
    if r.status_code >= 400:
        return 0

    data = r.json()["data"]["children"][0]["data"]

    return data["subreddit_subscribers"]
