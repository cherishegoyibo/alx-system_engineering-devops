#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    If not a valid subreddit, print None.
    """
    res = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if res.status_code == 200:
        for get_data in res.json().get("data").get("children"):
            print(get_data.get"data").get("title"))
    else:
        print(None)
