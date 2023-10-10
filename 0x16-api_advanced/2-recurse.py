#!/usr/bin/python3

"""
import
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    # Base case: if after is None, there are no more pages of results, return the hot_list
    if after is None:
        return hot_list

    # URL for the Reddit API to get the hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    # Set a custom User-Agent to avoid any issues
    headers = {'User-Agent': 'Custom User Agent'}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            # Extract and append the titles of the hot posts to the hot_list
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            # Recursively call the function with the 'after' parameter for pagination
            return recurse(subreddit, hot_list, data['data']['after'])
        except KeyError:
            # Invalid subreddit or unexpected JSON structure
            return None
    else:
        # Invalid subreddit or other API error
        return None

# Test the function
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
