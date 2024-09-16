from datetime import datetime

from task import Task
from json_db import db

class Tracker:
    def __init__(self):
        print(db.json)
        self.task_counter = db.json[-1].get('id') if db.json else 0

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
        type = "description"
        db.update_db(id,type, description)
        return f"Output: Task updated successfully (ID: {id})"

    def delete_task(self, id):
        """
            Deletes a task by id
        """
        db.delete_db(id)
        return f"Output: Task deleted successfully (ID: {id})"

        
        

tracker = Tracker()