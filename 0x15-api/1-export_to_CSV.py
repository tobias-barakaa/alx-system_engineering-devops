#!/usr/bin/python3

"""
Python script that exports data in the CSV format
"""

import requests
import sys
import csv

def export_todo_list_to_csv(employee_id):
    # API endpoints
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
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
                    csv_writer.writerow([task['userId'], employee_username, task['completed'], task['title']])

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
