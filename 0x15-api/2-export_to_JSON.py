#!/usr/bin/python3
""" for a given employee ID, returns
    information about his/her TODO list progress
"""


import requests
from sys import argv
import json


emp_id = argv[1]
tasks_count = 0

r_td = requests.get('https://jsonplaceholder.typicode.com/todos?userId='
                    + emp_id)
r_usr = requests.get('https://jsonplaceholder.typicode.com/users/'
                     + emp_id)

dictionary = {str(r_usr.json().get("id")): []}
for tasks in r_td.json():
    new_dict = {}
    user = r_usr.json()
    new_dict.update({"task": str(tasks.get("title")),
                                       "completed": tasks.get("completed"),
                                       "username": user.get("username")})
    dictionary[str(r_usr.json().get("id"))].append(new_dict)

f = open(str(r_usr.json().get("id")) + ".JSON", "w")
json.dump(dictionary, f)
# f.write(str(dictionary))
f.close()
