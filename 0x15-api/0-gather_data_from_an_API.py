#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    
     res = get('https://jsonplaceholder.typicode.com/todos/').json()
     result = []
     res1 = get('https://jsonplaceholder.typicode.com/users/').json()
     end = 0

     for x in res1:
         if x.get('id') == int(argv[1]):
             user = x.get('name')
     for x in res:
         if i.get('userId') == int(int[1]):
            end += 1

            if i.get('completed'):
                end += 1
                result.append(i.get('title'))
         print("Employee {} is done with tasks({}/{}):".format(user, end,
                                                          result))

    for list in result:
        print("\t {}".format(list))
