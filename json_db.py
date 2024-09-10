import json
import os


class JSONDB:
    def __init__(self):
        self.cwd = os.getcwd()
        self.filename = 'tracker.json'
        self.filepath = os.path.join(self.cwd, self.filename)
        self.json = self.read_db()

    def read_db(self):
        if not os.path.exists(self.filepath):
            return 'No task to do!'
        with open(self.filepath) as f:
            return json.load(f)
    
    def write_db(self, data):
        with open(self.filepath, 'a') as f:
            json.dump(data, f)


me = JSONDB()
#print(me.write_db('dddddd'))
#print(me.read_db())
