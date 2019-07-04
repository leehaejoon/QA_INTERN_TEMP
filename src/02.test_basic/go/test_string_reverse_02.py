import re
import string_reverse_05
import unittest
import os

test_word = '123'
testfile = 'test.txt'

class test_string_reverse_05(unittest.TestCase):


    def setUp(self):
        f = open(testfile,'w')
        f.write("".join('123'))
        f.close()

    def test_read_file(self):
        leng = string_reverse_05.read_file(testfile)
        self.assertEqual(leng,'123')

    def test_line_reverse(self):
        # '#' 없을시 test 용
        leng = string_reverse_05.line_reverse(test_word)
        self.assertEqual(leng[0], '321')
        # '#' 존재할시 test 용
        # leng = result.line_reverse('# 123')
        # self.assertEqual(leng[0], '# 321')

    def test_write_file(self):

        out_list = [test_word]
        string_reverse_05.write_file(testfile,out_list)
        leng = string_reverse_05.read_file(testfile)
        self.assertEqual(leng, '123')
    def tearDown(self):
        try:
            os.remove(test_result.testfile)
        except:
            pass




if __name__ == '__main__':
    unittest.main()



