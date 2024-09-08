#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if not subreddit or not isinstance(subreddit, str):
        return 0

    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = get(url, headers=headers, timeout=10)
	if response.status_code != 200:
	return 0

	data = response.json().get('data', {})
	return data.get('subscribers', 0)

    except Exception as e:
        return 0
