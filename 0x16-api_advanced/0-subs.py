#!/usr/bin/python3
"""
    Function Sub
"""
import json
import requests


def number_of_subscribers(subreddit):

    url = 'https://www.reddit.com/'
    url_subreddit = (url + '/r/' + subreddit + '/about.json')
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

    r_subreddit = requests.get(url_subreddit, headers=headers)
    obj_subreddit = r_subreddit.json()

    if r_subreddit.status_code == 200:
        subscribers = obj_subreddit['data']['subscribers']
        return (subscribers)
    else:
        return 0
