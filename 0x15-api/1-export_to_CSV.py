#!/usr/bin/python3
"""Export to CSV"""
import requests
import sys
import csv


def f_csv(users=None, todos=None):
    data = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(sys.argv[1] + ".csv", "w") as File:
        write = csv.DictWriter(File, fieldnames=data)
        for row in todos:
            write.writerow({"USER_ID": i.get("userId"),
                            "USERNAME": users[0].get("username"),
                            "TASK_COMPLETED_STATUS": i.get("completed"),
                            "TASK_TITLE": i.get("title")})

if __name__ == "__main__":
    """[Function initial]"""
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        args = {"id": sys.argv[1]}
        users = requests.get("https://jsonplaceholder.typicode.com/users",
                             params=args).json()
        args = {"userId": sys.argv[1]}
        todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                             params=args).json()
        done_task = 0
        number_task = []
        for i in todos:
            if i.get("completed"):
                number_task.append(i)
                done_task += 1

        print("Employee {} is done with tasks({}/{}):".format(
              users[0].get("name"), done_task, len(todos)))

        for i in number_task:
            print("\t {}".format(i.get("title")))
    f_csv(users, todos)
