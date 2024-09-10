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
            return f.read()
    
    def write_db(self):
        ...


me = JSONDB()
print(me.json)
