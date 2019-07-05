import re
import register_user_04
import unittest
import os
import sqlite3
import sys

test_USER_ID= 'olleh'
#testfile = 'test.txt' 이걸 db파일로 하기!
test_DB_file = 'test_user_info.db'
class test_register_user_01(unittest.TestCase):


    def setUp(self):#파일 미리 만들어 두기니까 미리 write해놓자
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



    # def test_read_file(self):
    #     leng = string_reverse_05.read_file(testfile)
    #     self.assertEqual(leng,'123')

    # def test_line_reverse(self):
    #     # '#' 없을시 test 용
    #     leng = string_reverse_05.line_reverse(test_word)
    #     self.assertEqual(leng[0], '321')
        # '#' 존재할시 test 용
        # leng = result.line_reverse('# 123')
        # self.assertEqual(leng[0], '# 321')

    # def test_write_file(self):
    #
    #     out_list = [test_word]
    #     string_reverse_05.write_file(testfile,out_list)
    #     leng = string_reverse_05.read_file(testfile)
    #     self.assertEqual(leng, '123')




if __name__ == '__main__':
    unittest.main()



