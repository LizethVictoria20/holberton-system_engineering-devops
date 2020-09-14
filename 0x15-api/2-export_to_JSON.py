#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
import sys


def f_json(users=None, todos=None, userId=None):
    """Export to CSV"""
    data = []
    with open(sys.argv[1] + ".json", "w") as file:
        for i in todos:
            data.append({"task": i.get("title"),
                         "completed": i.get("completed"),
                         "username": users[0].get("username")})
            file_json = {str(userId): data}
            json.dump(file_json, file)

if __name__ == "__main__":
    """[Function initials]"""
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        args_id = {"id": sys.argv[1]}
        users = requests.get("https://jsonplaceholder.typicode.com/users",
                             params=args_id).json()
        args_userid = {"userId": sys.argv[1]}
        todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                             params=args_userid).json()
        done_task = 0
        number_task = []
        for i in todos:
            if i.get("completed"):
                number_task.append(i)
                done_task += 1
            f_json(users, todos, sys.argv[1])
