#!/usr/bin/python3
"""script that queries subscribers on a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """gets the number of subscribers for a subreddit"""
    reddit_url = "https://www.reddit.com/r/{}/about.json" \
        .format(subreddit)

    header = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url,
                            headers=header
                            )

    if response.status_code == 200:
        data = response.json()['data']
        subs = data['subscribers']
        return subs
    return 0
