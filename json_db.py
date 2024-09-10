import os


class JSONDB:
    def __init__(self):
        self.cwd = os.getcwd()
        self.filepath = 'tracker.json'
        self.json = self.read_db()

    def read_db(self):
        with open(os.path.join(self.cwd, self.filepath), 'a') as f:
            f.write('[]')


me = JSONDB()
