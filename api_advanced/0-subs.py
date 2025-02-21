#!/usr/bin/python3
"""
Script that queries the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Gets the number of subscribers for a subreddit."""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    headers = {'User-Agent': 'Mozilla/5.0'}  # Using a browser-like User-Agent
    response = requests.get(reddit_url, headers=headers, allow_redirects=False)  # Prevents unwanted redirects

    if response.status_code == 200:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)  # Uses .get() to avoid KeyErrors

    return 0

