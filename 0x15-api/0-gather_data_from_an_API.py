#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    # Fetch TODO list data from the API
    todo_list = get('https://jsonplaceholder.typicode.com/todos/').json()
    
    # Initialize variables
    result = []
    user = None
    end = 0

    # Fetch user data from the API
    user_data = get('https://jsonplaceholder.typicode.com/users/').json()
    
    # Find the user by ID in user_data
    for x in user_data:
        if x.get('id') == int(argv[1]):
            user = x.get('name')

    # Iterate through TODO list data to count tasks
    for i in todo_list:
        if i.get('userId') == int(argv[1]):
            end += 1

            if i.get('completed'):
                end += 1
                result.append(i.get('title'))

    # Print the summary
    print("Employee {} is done with tasks({}/{}):".format(user, end, len(todo_list)))

    # Print the task titles
    for task in result:
        print("\t{}".format(task))
