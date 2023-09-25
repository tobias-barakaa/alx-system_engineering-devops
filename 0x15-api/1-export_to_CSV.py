#!/usr/bin/python3

"""
CSV Data Exporter

This Python script exports data in CSV format for a given employee
ID using a REST API.

Usage:
    python script.py <employee_id>

Dependencies:
    - requests
    - csv

The script fetches the user's data and their TODO list from the API,
and exports it to a CSV file.
"""

import csv
import requests
import sys


def export_todo_list_to_csv(employee_id):
    """
    Export TODO List to CSV for a given employee.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        None
    """
    # API endpoints
    empId = employee_id
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={empId}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    try:
        # Fetch user data
        user_response = requests.get(user_url)
        user_data = user_response.json()

        if 'username' not in user_data:
            print(f"Employee with ID {employee_id} not found.")
            return

        employee_username = user_data['username']

        # Fetch TODO list data for the user
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        csv_filename = f'{employee_id}.csv'

        with open(csv_filename, 'w', newline='') as file:
            csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

            for task in todos_data:
                if 'userId' in task:
                    csv_writer.writerow([task['userId'], employee_username,
                                         task['completed'], task['title']])

        print(f"Data exported to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_todo_list_to_csv(employee_id)
