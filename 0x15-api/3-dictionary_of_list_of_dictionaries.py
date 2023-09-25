#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""
import json
import requests

def export_json():
    """Exports data in JSON format for all users.

    Returns:
    A dictionary containing the TODO items for all users.
    """

    # Get the TODO items for all users.
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()

    # Get the users.
    response = requests.get('https://jsonplaceholder.typicode.com/users/')
    users = response.json()

    # Create a dictionary to store the TODO items for all users.
    user_todos = {}
  for user in users:
    user_todos[user['id']] = []

  # Add the TODO items to the dictionary for each user.
  for todo in todos:
    user_todos[todo['userId']].append({
      'username': users[todo['userId'] - 1]['username'],
      'task': todo['title'],
      'completed': todo['completed']
    })

    return user_todos

if __name__ == '__main__':
  # Export the data in JSON format.
    user_todos = export_json()

  # Write the JSON data to a file
  with open('todo_all_employees.json', 'w') as f:
      json.dump(user_todos, f)
