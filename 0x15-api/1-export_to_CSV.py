#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

def get_todo_list_progress(user_id):
    # API endpoints
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'

    try:
        # Fetch user data
        user_response = requests.get(user_url)
        user_data = user_response.json()

        if 'name' not in user_data:
            print(f"Employee with ID {user_id} not found.")
            return

        user_name = user_data['name']

        # Fetch TODO list data for the user
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task['completed']]
        total_tasks = len(todos_data)

        print(f"Employee {user_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)
