#!/usr/bin/python3

"""
Function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subcribers (not active users, total subscribers) for a given subreddit.
    If not a valid subreddit, return 0.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    res = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Google Chrome Version 81.0.4044.129"},
    )

    try:
        return res.json().get("data").get("subscribers")
    else:
        return 0
