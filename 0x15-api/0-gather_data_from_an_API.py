#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress """
import requests
import sys

if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    response_user = requests.get(url)
    emp_data = response_user.json()
    emp_name = emp_data['name']

    url_todo = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    emp_todo = (requests.get(url_todo)).json()

    total_tasks = len(emp_todo)
    done_tasks = sum(1 for task in emp_todo if task['completed'])

    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, done_tasks, total_tasks))
    for task in emp_todo:
        if task['completed']:
            print("\t {}".format(task['title']))
