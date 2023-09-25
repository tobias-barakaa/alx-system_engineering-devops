#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv

def get_employee_todo_progress(employee_id):
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    completed = 0
    total = 0
    tasks = []

    for i in data:
        if i.get('userId') == int(employee_id):
            total += 1

            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))

    return {
        "employee_name": employee_id,
        "number_of_done_tasks": completed,
        "total_number_of_tasks": total,
        "task_titles": tasks
    }

if __name__ == "__main__":
    employee_id = int(argv[1])
    employee_todo_progress = get_employee_todo_progress(employee_id)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_todo_progress["employee_name"],
        employee_todo_progress["number_of_done_tasks"],
        employee_todo_progress["total_number_of_tasks"]
    ))

    for task_title in employee_todo_progress["task_titles"]:
        print("\t {}".format(task_title))
