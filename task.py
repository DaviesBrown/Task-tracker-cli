from datetime import datetime
from uuid import uuid4
from enum import Enum

class Status(Enum):
    TODO = 'todo'
    INPROGRESS = 'in-progress'
    DONE = 'done'

print(Status.DONE.value)


class Task:
    def __init__(self, id, description):
        self.id = id #str(uuid4())
        self.description = description
        self.status = Status.TODO.value
        self.createdAt = datetime.now().strftime('%c')
        self.updatedAt = self.createdAt

    def get_task(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
