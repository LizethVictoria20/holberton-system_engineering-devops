#!/usr/bin/python3
import json
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/'
    url_subreddit = (url + '/r/' + subreddit + '/hot.json?limit=10')
    headers = {"User-Agent": "Client"}

    # Get data response whit requests
    r_subreddit = requests.get(url_subreddit, headers=headers)
    if r_subreddit.status_code != 200:
        print('None')
        return 0

    # Set string to JSON
    obj_subreddit = r_subreddit.json()

    # Print number of children
    for children in obj_subreddit['data']['children']:
        print(children['data']['title'])