#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress then exports data in
the JSON format"""
import json
import requests

if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users"
    response_user = requests.get(url)
    emp_data = response_user.json()

    all_emp_json = {}

    for emp in emp_data:
        emp_id = emp['id']
        emp_name = emp['username']
        url_tod = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
        emp_todo = (requests.get(url_tod)).json()

        tasks = []
        for task in emp_todo:
            tasks.append({
                "username": emp_name,
                "task": task['title'],
                "completed": task['completed']
                })
        all_emp_json[emp_id] = tasks

    jsonfile = "todo_all_employees.json"
    with open(jsonfile, 'w') as myfile:
        json.dump(all_emp_json, myfile)
