import re
import result
import unittest
import os

test_word = '123'
testfile = 'test.txt'

class test_result(unittest.TestCase):


    def setUp(self):
        f = open(testfile,'w')
        f.write("".join('123'))
        f.close()

    def test_read_file(self):
        leng = result.read_file(testfile)
        self.assertEqual(leng,'123')

    def test_line_reverse(self):
        # '#' 없을시 test 용
        leng = result.line_reverse(test_word)
        self.assertEqual(leng[0], '321')
        # '#' 존재할시 test 용
        # leng = result.line_reverse('# 123')
        # self.assertEqual(leng[0], '# 321')

    def test_write_file(self):

        out_list = [test_word]
        result.write_file(testfile,out_list)
        leng = result.read_file(testfile)
        self.assertEqual(leng, '123')
    def tearDown(self):
        try:
            os.remove(test_result.testfile)
        except:
            pass




if __name__ == '__main__':
    unittest.main()



