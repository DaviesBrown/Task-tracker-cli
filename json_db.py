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


db = JSONDB()
""" print(db.json)
db.write_db({'dd': 'ggg'})
print(db.read_db()) """
