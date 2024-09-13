from task import Task
from json_db import db

class Tracker:
    def __init__(self):
        self.task_counter = db.json[-1]['id']

    def create_task(self, description):
        id = self.task_counter + 1
        self.task_counter = id
        task = Task(id=id, description=description)
        db.write_db(task.get_task())
        return f"Output: Task added successfully (ID: {task.id})"

tracker = Tracker()