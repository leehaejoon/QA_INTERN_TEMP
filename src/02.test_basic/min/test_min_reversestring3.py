import re
import unittest

def revers_string(srcFile_name, resultFile_name):
    srcFile = open(srcFile_name, "rt", encoding="UTF-8")
    resultFile =  open(resultFile_name, "wt", encoding="UTF-8")
    s=re.compile("\w+")
    with srcFile, resultFile:
        for line in srcFile:
            only_list = s.findall(line)
            only_string = " ".join(only_list)
            re_string = only_string[::-1]
            output=line.replace(only_string, re_string)
            resultFile.write(output)
            return output


class test_reveres_string (unittest.TestCase):
    def setUp(self):
        self.srcFile_name = 'test_3_sample.txt'
        self.resultFile_name = 'test_3_result.txt'
        self.test_word = "# 줄째첫"
        srcFile = open(self.srcFile_name, "wt", encoding="UTF-8")
        srcFile.write(self.test_word)
        srcFile.close()

    def tearDown(self):
        pass

    def test_runs(self):
        revers_string('test_3_sample.txt', 'test_3_result_real.txt')

    def test_revers_string_function(self):
        self.assertEqual(revers_string(self.srcFile_name, self.resultFile_name), '# 첫째줄')


if __name__ == "__main__":
    unittest.main()
