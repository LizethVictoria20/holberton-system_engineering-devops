#!/usr/bin/python3
"""Dictionary of list of dictionaries """
import json
import requests
import sys


def f_json(users=None, todos=None):
    """Export to CSV"""
    list_json = []
    data = {}
    with open("todo_all_employees.json", "w") as file:
        for i in users:
            u = i.get("id")
            for i in todos:
                if u == i.get("userId"):
                    list_json.append({"username": users[0].get("username"),
                                      "task": i.get("title"),
                                      "completed": i.get("completed")})
            data[u] = list_json
        json.dump(data, file)

if __name__ == "__main__":
    """[Function initial]"""
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    f_json(users, todos)
