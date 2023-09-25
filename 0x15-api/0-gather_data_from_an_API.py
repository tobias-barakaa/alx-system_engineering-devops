#!/usr/bin/python3
"""
Script to Fetch Employee TODO List Progress

This script accepts an employee ID as a parameter and retrieves information
about the employee's TODO list progress from a REST API. It fetches data from
the 'jsonplaceholder.typicode.com' API and displays the progress in a specific format.

Usage:
    python3 gather_data_from_an_API.py <employee_id>

Parameters:
    - <employee_id>: An integer representing the employee's ID.

Example:
    To check the TODO list progress for an employee with ID 2:
    python3 gather_data_from_an_API.py 2

The script uses the 'requests' library to make an HTTP GET request to the API
and calculates the number of completed and total tasks. It then displays the
employee's progress in the following format:

Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

Author: [Your Name]
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    try:
        response_data = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
        response_data.raise_for_status()
        todo_data = response_data.json()

        if not todo_data:
            print(f"No TODO data found for employee with ID {employee_id}")
            return

        user_data = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        user_data.raise_for_status()
        user_info = user_data.json()

        completed_tasks = sum(1 for task in todo_data if task['completed'])
        total_tasks = len(todo_data)

        print(f"Employee {user_info['name']} is done with tasks({completed_tasks}/{total_tasks}):")
        for task in todo_data:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
