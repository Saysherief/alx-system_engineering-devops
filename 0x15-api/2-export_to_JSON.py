#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress then exports data in
the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    response_user = requests.get(url)
    emp_data = response_user.json()
    emp_name = emp_data['username']

    url_todo = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    emp_todo = (requests.get(url_todo)).json()

    emp_json = {
            f"{emp_id}": []
            }

    for task in emp_todo:
        emp_json[f"{emp_id}"].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": emp_name
            })

    jsonfile = f"{emp_id}.json"
    with open(jsonfile, 'w') as myfile:
        json.dump(emp_json, myfile)
