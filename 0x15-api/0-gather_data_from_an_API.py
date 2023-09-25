#!/usr/bin/python3
"""
Script to Fetch Employee TODO List Progress

This script accepts an employee ID as a parameter and retrieves information
about the employee's TODO list progress from a REST API. It fetches data from
the 'jsonplaceholder.typicode.com' API and displays the progress in a specific format.

Usage:
    python3 gather_data_from_an_API.py <employee_id>

Parameters:
    - <employee_id>: An integer representing the employee's

Example:
    To check the TODO list progress for an employee with ID 2:
    python3 gather_data_from_an_API.py 2

The script uses the 'requests' library to make HTTP GET requests to the API
and calculates the number of completed and total tasks. It then displays the
employee's progress in the following format:

Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

Author: [Your Name]
"""

from requests import get
from sys import argv

def get_employee_todo_progress(employee_id):
    response_data = get("https://jsonplaceholder.typicode.com/todos")
    user_data = get("https://jsonplaceholder.typicode.com/users").json()
    res_data = response_data.json()
    completed = 0
    result = []
    all = 0
    if res_data is not False:
        for i in res_data:
            if i.get('userId') == int(argv[1]):
                all += 1
        for i in user_data:
            if i.get('id') == int(argv[1]):
                user = i.get('name')
            elif i.get('completed') is not False:
                user += 1
                result.append(i.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(user, completed,
                                                          all))

    for i in result:
        print("\t {}".format(i))
