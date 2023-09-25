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
import csv
from sys import argv

if __name__ == "__main__":
    employee_id = int(argv[1])

    # Fetch employee data from the REST API
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get('username')

    # Fetch TODO list data from the REST API
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create a CSV file for the employee
    csv_filename = f'{employee_id}.csv'
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        # Write the tasks owned by the employee to the CSV file
        for task in todos_data:
            if task['userId'] == employee_id:
                task_completed = str(task['completed'])
                task_title = task['title']
                csv_writer.writerow([employee_id, employee_name, task_completed, task_title])

    print(f"Data has been exported to {csv_filename}.")
