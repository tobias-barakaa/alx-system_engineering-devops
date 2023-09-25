#!/usr/bin/python3

import requests
import csv
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
