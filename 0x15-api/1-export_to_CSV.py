#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress then exports data in
the CSV format"""
import csv
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

    emp_csv = []
    for task in emp_todo:
        emp_csv.append([emp_id, emp_name, str(
            task['completed']), task['title']])

    csvfile = f"{emp_id}.csv"
    with open(csvfile, 'w', newline='') as myfile:
        writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        writer.writerows(emp_csv)
