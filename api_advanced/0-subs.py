#!/usr/bin/python3
"""script that queries subscribers on a subreddit"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    Returns 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom-script:v1.0 (by /u/yourusername)"}  # Use a custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0

# Example usage
if __name__ == "__main__":
    subreddit = "python"  # Change this to any subreddit you want to test
    print(f"Number of subscribers: {number_of_subscribers(subreddit)}")

