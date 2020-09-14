#!/usr/bin/python3
"""Export to CSV"""
import csv
import requests
import sys


def f_csv(users=None, todos=None):
    """Export to CSV"""
    data = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(sys.argv[1] + ".csv", "w") as file:
        write = csv.DictWriter(file, fieldnames=data, quoting=csv.QUOTE_ALL)
        for i in todos:
            write.writerow({"USER_ID": i.get("userId"),
                            "USERNAME": users[0].get("username"),
                            "TASK_COMPLETED_STATUS": i.get("completed"),
                            "TASK_TITLE": i.get("title")})

if __name__ == "__main__":
    """[Function initial]"""
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
            f_csv(users, todos)
