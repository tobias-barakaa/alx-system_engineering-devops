#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    all = 0
    res = get('https://jsonplaceholder.typicode.com/todos/').json()
    result = []
    res1 = get('https://jsonplaceholder.typicode.com/users/').json()

    for i in res1:
        if i.get('id') == int(argv[1]):
            users = i.get('name')
        elif i.get('userId') == int(argv[1]):
            all += 1
        elif i.get('completed') is not False:
            all += 1
            result.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(users, all, len(res)))

    for i in result:
        print("\t{}".format(i))
