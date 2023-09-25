#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

import requests
import sys
import json

def export_todo_list_to_json(user_id):
    # API endpoints
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'

    try:
        # Fetch user data
        user_response = requests.get(user_url)
        user_data = user_response.json()

        if 'username' not in user_data:
            print(f"Employee with ID {user_id} not found.")
            return

        username = user_data['username']

        # Fetch TODO list data for the user
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        user_dict = {}
        user_dict[username] = []

        for task in todos_data:
            if 'userId' in task:
                user_dict[username].append({
                    'task': task['title'],
                    'completed': task['completed']
                })

        with open(f'{user_id}.json', 'w') as json_file:
            json.dump(user_dict, json_file, indent=4)

        print(f"Data exported to {user_id}.json")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    export_todo_list_to_json(user_id)
