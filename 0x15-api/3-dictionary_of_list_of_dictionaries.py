#!/usr/bin/python3
"""Dictionary of list of dictionaries """
import json
import requests
import sys


def f_json(users=None, todos=None):
    """Export to CSV"""
    data = []
    list_json = {}
    with open("todo_all_employees.json", "w") as f:
        for i in users:
            u = i.get("id")
            for i in todos:
                if u == i.get("userId"):
                    data.append({"username": users[0].get("username"),
                                 "task": i.get("title"),
                                 "completed": i.get("completed")})
            list_json[u] = data
        json.dump(list_json, f)

if __name__ == "__main__":
    """[Function initials]"""
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    make_all(users, todos)
