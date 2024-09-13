import unittest
import os

from json_db import JSONDB

class JSONDBTestCase(unittest.TestCase):
    def setUp(self):
        self.test_db = JSONDB()
    
    """ def tearDown(self):
        if os.path.exists("test.json"):
            os.remove("test.json")
 """
    def test_read_from_json_file(self):
        self.assertEqual(self.test_db.filepath, f'{os.getcwd()}\\test.json')
        self.assertEqual(self.test_db.json, None)
    
    def test_write_to_json_file(self):
        self.test_db.write_db('HELLO')
        self.assertEqual(self.test_db.json, ["HELLO"])
        self.test_db.write_db('HELLO')
        self.assertEqual(self.test_db.json, ["HELLO", "HELLO"])

unittest.main()