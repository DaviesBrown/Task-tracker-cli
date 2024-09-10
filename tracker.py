from task import Task
from json_db import db

class Tracker:
    def create_task(self, description):
        task = Task(description=description)
        db.write_db(task.get_task())
        return f"Output: Task added successfully (ID: {task.id})"

tracker = Tracker()