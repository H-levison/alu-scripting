#!/usr/bin/python3 
"""
This script contains a function that queries the Reddit API to retrieve the number of subscribers for a given subreddit.
It ensures handling of invalid subreddits by returning 0 in such cases and avoids following redirects.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom-script/1.0"}  # Setting a custom User-Agent to avoid Too Many Requests error

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0
