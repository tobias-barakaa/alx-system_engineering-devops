#!/usr/bin/python3
"""
Script to Fetch Employee TODO List Progress

This script accepts an employee ID as a parameter and retrieves information
about the employee's TODO list progress from a REST API. It fetches data from
the 'jsonplaceholder.typicode.com' API and displays
the progress in a specific format.

Usage:
    python3 gather_data_from_an_API.py <employee_id>

Parameters:
    - <employee_id>: An integer representing the employee's ID.

Example:
    To check the TODO list progress for an employee with ID 2:
    python3 gather_data_from_an_API.py 2

The script uses the 'requests' library to make HTTP GET requests to the API
and calculates the number of completed and total tasks. It then displays the
employee's progress in the following format:

Employee EMPLOYEE_NAME is done with tasks
(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

Author: [Your Name]
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Parse the employee ID from command line arguments
    employee_id = int(argv[1])

    # Fetch employee data from the REST API
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get('name')

    # Fetch TODO list data from the REST API
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = 0
    completed_tasks = 0
    completed_task_titles = []

    # Iterate through the TODO list to count completed tasks and collect titles
    for task in todos_data:
        if task['userId'] == employee_id:
            total_tasks += 1
            if task['completed']:
                completed_tasks += 1
                completed_task_titles.append(task['title'])

    # Display progress in the specified format
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                         completed_tasks, total_tasks))
    for title in completed_task_titles:
        print("\t {}".format(title))
