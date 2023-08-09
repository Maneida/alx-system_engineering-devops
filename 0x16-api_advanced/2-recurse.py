#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles of
all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns list containing titles of all hot articles for given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    if after:
        params = {"after": after}
    else:
        params = None

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if len(posts) == 0:
            return None  # No posts found
        else:
            for post in posts:
                hot_list.append(post['data']['title'])

            after = data["data"]["after"]
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list

    elif response.status_code == 404:
        return None

    else:
        print("Error: Status Code {}".format(response.status_code))
        return None
