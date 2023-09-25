#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

import requests
import json

def export_todo_list_to_json():
    # Fetch TODO list data and user data
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = todos_response.json()

    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = users_response.json()

    # Create a dictionary to store user tasks
    user_tasks = {}

    for user in users_data:
        user_id = user['id']
        username = user['username']

        # Filter tasks for this user
        user_tasks[user_id] = []

        for task in todos_data:
            if task['userId'] == user_id:
                user_tasks[user_id].append({
                    'username': username,
                    'task': task['title'],
                    'completed': task['completed']
                })

    # Write data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_tasks, json_file, indent=4)

    print("Data exported to todo_all_employees.json")

if __name__ == "__main__":
    export_todo_list_to_json()
