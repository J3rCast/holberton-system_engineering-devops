#!/usr/bin/python3
"""This file contains a function that queries the Reddit API"""


import requests


def recurse_titles(subreddit, hot_list=[], count = 0, after=None):
    """ returns a list containing the titles of all
        hot articles for a given subreddit"""

    if after == None:
        url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(
            subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
            subreddit, after)

    headers = {'User-Agent': 'My User Agent 1.0'}

    r = requests.get(url, headers=headers)
    if r.status_code >= 400:
        return None

    data = r.json()["data"]["children"]

    if count < len(data):
        hot_list.append(data[count]["data"]["title"])
        return recurse_titles(subreddit, hot_list, count + 1)
    return hot_list

def recurse(subreddit, hot_list=[], after=None):
    """ returns a list containing the titles of all
        hot articles for a given subreddit"""

    if after == None:
        url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(
            subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
            subreddit, after)

    headers = {'User-Agent': 'My User Agent 1.0'}

    hot_list.append(recurse_titles(subreddit, hot_list, 0, after))
    if hot_list == None:
        return None

    r = requests.get(url, headers=headers)

    after = r.json()["data"]["after"]

    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list
