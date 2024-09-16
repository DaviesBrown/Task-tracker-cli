from datetime import datetime
import json
import os


class JSONDB:
    def __init__(self) -> None:
        self.cwd = os.getcwd()
        self.filename = 'tracker.json'
        self.filepath = os.path.join(self.cwd, self.filename)
        self.json = self.read_db()

    def read_db(self):
        try:
            with open(self.filepath) as f:
                return json.load(f)
        except FileNotFoundError:
            print('No task to do!')
    
    def write_db(self, data):
        if not self.json:
            with open(self.filepath, 'w') as f:
                self.json = [data]
                json.dump(self.json, f)
        else:
            with open(self.filepath, 'w') as f:
                self.json.append(data)
                json.dump(self.json, f)

    def delete_db(self, id):
        self.json = [task for task in db.json if task["id"] != int(id)]
        with open(self.filepath, 'w') as f:
            json.dump(self.json, f)
    
    def update_db(self, id, type, data):
        lookup = [task for task in db.json if task["id"] == int(id)][0]
        old = lookup
        lookup[type] = data
        lookup["updatedAt"] = datetime.now().strftime('%c')
        db.json.remove(old)
        db.write_db(lookup)


db = JSONDB()
""" print(db.json)
db.write_db({'dd': 'ggg'})
print(db.read_db()) """
