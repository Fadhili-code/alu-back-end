#!/usr/bin/python3
"""Script to fetch and display TODO list progress of an employee."""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Get user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user = user_response.json()
    employee_name = user.get("name")

    # Get todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Count completed tasks
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_count = len(done_tasks)

    # Print header
    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_count, total_tasks))

    # Print completed task titles
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
