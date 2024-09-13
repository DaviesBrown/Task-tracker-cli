from datetime import datetime

from task import Task
from json_db import db

class Tracker:
    def __init__(self):
        self.task_counter = db.json[-1]['id'] if db.json else 0

    def create_task(self, description):
        """
            Creates a task from a description and writes it to a json file
        """
        id = self.task_counter + 1
        self.task_counter = id
        task = Task(id=id, description=description)
        db.write_db(task.get_task())
        return f"Output: Task added successfully (ID: {task.id})"

    def update_task(self, id, description):
        """
            Updates a task from the json file based on id
        """
        data = [task for task in db.json if task["id"] == int(id)]
        old = data[0]
        data[0]["description"] = description
        data[0]["updatedAt"] = datetime.now().strftime('%c')
        db.json.remove(old)
        db.write_db(data[0])
        print(data[0])

tracker = Tracker()