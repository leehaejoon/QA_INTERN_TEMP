import re
import register_user_04
import unittest
import os
import sqlite3
import sys

test_USER_ID= 'olleh'
test_DB_file = 'test_user_info.db'

class test_register_user_01(unittest.TestCase):
    def setUp(self):
        conn = sqlite3.connect(test_DB_file)
        cur = conn.cursor()
        cur.execute('''CREATE table REGISTER_DATE (USER_ID,yesy,month,day,hour,min,second)''')
        conn.close()

    def test_input_db(self):
        list = register_user_04.input_db(test_USER_ID, test_DB_file)
        self.assertEqual(list[0][0],test_USER_ID)

    def tearDown(self):
        try:
            os.remove(test_DB_file)
        except:
            pass

if __name__ == '__main__':
    unittest.main()




