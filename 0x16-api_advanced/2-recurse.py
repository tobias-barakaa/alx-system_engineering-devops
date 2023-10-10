#!/usr/bin/python3
"""import"""

import requests

def get_hot_posts(subreddit, limit=100):
  """Queries the Reddit API and returns a list of the titles of the
  hot posts listed for a given subreddit.

  Args:
    subreddit: The name of the subreddit to get the hot posts for.
    limit: The maximum number of hot posts to return.

  Returns:
    A list of the titles of the hot posts.
  """

  headers = {'User-Agent': 'DiegoOrejuela'}
  params = {"limit": limit}
  response = requests.get("https://www.reddit.com/r/{}/hot/.json".
                          format(subreddit), headers=headers, params=params)
  if response:
    hot_list = []
    for title in response.json().get("data").get("children"):
      hot_list.append(title.get("data").get("title"))
    return hot_list
  else:
    return None

def main():
  subreddit = input("Enter the name of a subreddit: ")
  hot_posts = get_hot_posts(subreddit)
  if hot_posts:
    print("The hot posts for the subreddit {} are:".format(subreddit))
    for post in hot_posts:
      print(post)
  else:
    print("No hot posts found for the subreddit {}".format(subreddit))

if __name__ == '__main__':
  main()
