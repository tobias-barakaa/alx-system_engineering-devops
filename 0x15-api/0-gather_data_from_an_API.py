#!usr/bin/python3
"""
script to fetch to do list
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
            
            # Display the employee's TODO list progress
            print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
            
            # Display the titles of completed tasks
            for task in todo_data:
                if task['completed']:
                    print(f"\t{task['title']}")
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
