#!/usr/bin/python3
import json
import requests

def get_employee_todo_list_progress(employee_id):
  """
  Returns information about the given employee's TODO list progress.

  Args:
    employee_id (int): The ID of the employee.

  Returns:
    A dictionary containing the following information:
      * employee_name (str): The name of the employee.
      * number_of_done_tasks (int): The number of completed tasks.
      * total_number_of_tasks (int): The total number of tasks.
      * task_titles (list[str]): A list of the titles of the completed tasks.
  """

  url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
  response = requests.get(url)

  if response.status_code != 200:
    raise Exception("Failed to get employee information: {}".format(response.status_code))

  employee_data = json.loads(response.content)

  # Get the employee's name.
  employee_name = employee_data["name"]

  # Get the employee's TODO list.
  todo_list_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
  todo_list_response = requests.get(todo_list_url)

  if todo_list_response.status_code != 200:
    raise Exception("Failed to get employee TODO list: {}".format(todo_list_response.status_code))

  todo_list_data = json.loads(todo_list_response.content)

  # Count the number of completed tasks.
  number_of_done_tasks = 0
  for task in todo_list_data:
    if task["completed"]:
      number_of_done_tasks += 1

  # Count the total number of tasks.
  total_number_of_tasks = len(todo_list_data)

  # Get the titles of the completed tasks.
  task_titles = []
  for task in todo_list_data:
    if task["completed"]:
      task_titles.append(task["title"])

  return {
    "employee_name": employee_name,
    "number_of_done_tasks": number_of_done_tasks,
    "total_number_of_tasks": total_number_of_tasks,
    "task_titles": task_titles
  }

def main():
  """
  The main function of the script.
  """

  # Get the employee ID from the user.
  employee_id = int(input("Enter the employee ID: "))

  # Get the employee's TODO list progress.
  employee_todo_list_progress = get_employee_todo_list_progress(employee_id)

  # Display the employee's TODO list progress on the standard output.
  print("Employee {} is done with tasks({}/{}):".format(employee_todo_list_progress["employee_name"], employee_todo_list_progress["number_of_done_tasks"], employee_todo_list_progress["total_number_of_tasks"]))
  for task_title in employee_todo_list_progress["task_titles"]:
    print("    {}".format(task_title))

if __name__ == "__main__":
  main()
