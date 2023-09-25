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

The script uses the 'requests' library to make HTTP GET requests to the API
and calculates the number of completed and total tasks. It then displays the
employee's progress for each task.

Author: [Your Name]
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the API URL with the employee_id parameter
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        employee_data = response.json()
        
        # Get the employee's name
        employee_name = employee_data['name']
        
        # Fetch the TODO list for the employee
        todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        todo_response = requests.get(todo_url)
        
        if todo_response.status_code == 200:
            todo_data = todo_response.json()
            
            # Calculate the number of completed and total tasks
            total_tasks = len(todo_data)
            completed_tasks = sum(1 for task in todo_data if task['completed'])
            
            # Display the employee's TODO list progress for each task
            for i, task in enumerate(todo_data, start=1):
                print(f"Task {i} Formatting: {'OK' if task['completed'] else 'Incorrect'}")
        else:
            print(f"Error: Unable to fetch TODO list for employee {employee_name}")
    else:
        print(f"Error: Unable to fetch employee data for ID {employee_id}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
