#!/usr/bin/python3
"""
    Function Sub
"""
import json
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/'
    url_subreddit = (url + '/r/' + subreddit + '/hot.json?limit=10')
    userAgent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

    r_subreddit = requests.get(url_subreddit, userAgent=userAgent)
    if r_subreddit.status_code != 200:
        print('None')
        return 0

    obj_subreddit = r_subreddit.json()

    for children in obj_subreddit['data']['children']:
        print(children['data']['title'])
