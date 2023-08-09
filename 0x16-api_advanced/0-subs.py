#!/usr/bin/python3
"""
Queries Reddit API and returns number of subscribers of a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Function that returns the number of subscribers of a given subreddit"""
    url = "https://www.reddit.com//r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    elif response.status_code == 404:
        return 0
    else:
        print("Error: Status code {}".format(response.status_code))
