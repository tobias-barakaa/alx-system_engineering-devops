#!/usr/bin/python3
"""Import"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """function that queries using recursion"""

    params = {"limit": 100, 'after': after}
    headers = {'User-Agent': 'DiegoOrejuela'}
    result = requests.get("https://www.reddit.com/r/{}/hot/.json".
                            format(subreddit), headers=headers, params=params)
    if result:
        after = result.json().get("data").get("after")
        if after:
            recurse(subreddit, hot_list, after=after)
            titles = result.json().get("data").get("children")
            for title in titles:
                hot_list.append(title.get("data").get("title"))
            return hot_list
        else:
            titles = result.json().get("data").get("children")
            for title in titles:
                hot_list.append(title.get("data").get("title"))
            return hot_list
    else:
        return None
