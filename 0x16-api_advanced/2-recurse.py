#!/usr/bin/python3

"""
import
"""


import requests
import sys

def get_hot_posts(subreddit):
  """Recursively gets the hot posts for a given subreddit.

  Args:
    subreddit: The name of the subreddit to get the hot posts for.

  Returns:
    A list of the titles of the hot posts.
  """

  after = None
  hotlist = []
  while True:
    headers = {'User-Agent': 'Dan Kazam'}
    if after:
      url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
          subreddit, after)
    else:
      url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    data = response.json().get('data')
    if not data:
      break
    hotlist += [dic.get('data').get('title') for dic in data.get('children')]
    after = data.get('after')
  return hotlist

if __name__ == '__main__':
  subreddit = sys.argv[1]
  hot_posts = get_hot_posts(subreddit)
  for post in hot_posts:
    print(post)
