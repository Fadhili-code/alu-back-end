#!/usr/bin/python3
"""Fetches and displays a user's TODO list progress using REST API"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Get user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user = user_response.json()
    employee_name = user.get("name")

    # Get TODO list for the user
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Get completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]

    # Print first line with correct formatting
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos)))

    # Print completed task titles, each properly formatted
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
