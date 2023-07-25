#!/usr/bin/python3
"""
Request from API; Return TODO list progress of all employees
Export this data to JSON
"""
import json
import requests


def all_to_json():
    """return API data"""
    try:
        USERS = []
        user_response = requests.get(
            "http://jsonplaceholder.typicode.com/users"
            )
        user_data = user_response.json()
        for u in user_data:
            USERS.append((u.get('id'), u.get('username')))
        TASK_STATUS_TITLE = []
        todos = requests.get("http://jsonplaceholder.typicode.com/todos")
        todo_data = todos.json()
        for t in todo_data:
            TASK_STATUS_TITLE.append((t.get('userId'),
                                      t.get('completed'),
                                      t.get('title')))

        """export to json"""
        data = dict()
        for u in USERS:
            t = []
            for task in TASK_STATUS_TITLE:
                if task[0] == u[0]:
                    t.append({"task": task[2],
                              "completed": task[1],
                              "username": u[1]})
            data[str(u[0])] = t
        filename = "todo_all_employees.json"
        with open(filename, "w") as f:
            json.dump(data, f, sort_keys=True)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    all_to_json()
