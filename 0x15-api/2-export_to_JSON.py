#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

# Documentation:
# This Python script is designed to fetch data from a public REST API and export it in JSON format.
# It retrieves a list of tasks associated with a specific employee ID from the JSONPlaceholder API
# and organizes the data into a JSON object. The JSON object is then written to a JSON file with
# the filename being the employee's ID.

# Usage:
# To use this script, run it from the command line with an employee ID as an argument. For example:
#   python3 script.py 2
# This will fetch the tasks associated with the employee ID 2 and export the data to a JSON file
# named "2.json" in the current directory.

# Requirements:
# - Python 3
# - The `requests` module for making HTTP requests. You can install it using pip:
#   pip install requests

import json
from requests import get
from sys import argv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for i in data2:
        if i['id'] == int(argv[1]):
            u_name = i['username']
            id_no = i['id']

    row = []

    for i in data:

        new_dict = {}

        if i['userId'] == int(argv[1]):
            new_dict['username'] = u_name
            new_dict['task'] = i['title']
            new_dict['completed'] = i['completed']
            row.append(new_dict)

    final_dict = {}
    final_dict[id_no] = row
    json_obj = json.dumps(final_dict)

    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)
