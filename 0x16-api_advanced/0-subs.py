#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Subreddit"""
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    head = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    request = requests.get(url, headers=head)
    if request.status_code != 200:
        return 0
    return request.json().get("data").get("subscribers")
