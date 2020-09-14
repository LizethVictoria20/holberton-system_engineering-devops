#!/usr/bin/python3
"""Dictionary of list of dictionaries """
import json
import requests


def f_json(users=None, todos=None):
    """Export to CSV"""
    data = []
    user_id = {}
    with open("todo_all_employees.json", "w") as file:
        for i in users:
            user = i.get("id")
            for i in todos:
                if user == i.get("userId"):
                    data.append({"username": users[0].get("username"),
                                 "task": i.get("title"),
                                 "completed": i.get("completed")})

            user_id[user] = data
        json.dump(user_id, file)

if __name__ == "__main__":
    """[Function initials]"""
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    f_json(users, todos)
