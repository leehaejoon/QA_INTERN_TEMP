import unittest

def find_hash(line):
    return line.count('#')

def find_left(line):
    return line.find('#')

def find_len(line):
    return len(line)

def set_hashLine(line, left, num):
    return line[left:num]

def set_strLine(line, num, left, right):
    return line[num-left:right]

def revers_str(reline):
    return reline[::-1]

def set_result(size, reline):
    return size + ' ' + reline.strip('\n')

def write_result(re_path, result):
     with open (re_path, 'w', encoding="UTF-8") as f:
            f.write(result)

def write_blank(re_path):
    with open (re_path, 'w', encoding="UTF-8") as f:
            f.write('\n')

def revers_string(src_path, re_path):
    src_file = open(src_path, "r", encoding='UTF-8')
    with src_file:
        for line in src_file:
            num = find_hash(line)
            left = find_left(line)
            right = find_len(line)
            if left > -1:
                size = set_hashLine(line, left, num)
                reline = set_strLine(line, num, left, right)
                reline = revers_str(reline)
                result = set_result(size, reline)
                write_result(re_path, result)
            else:
                write_blank(re_path)


class Test_revers_string(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.src_path = "test_sample.txt"
        self.re_path = "test_sample_result10.txt"

        self.line = '@ 줄째첫'
        with open(self.src_path, 'wt', encoding='UTF-8')as self.test_sample_file:
            self.test_sample_file.write(self.line)

        self.reline = revers_str('줄째첫')
        self.num = find_hash(self.line)
        self.left = find_left(self.line)
        self.right = find_len(self.line)
        self.size = set_hashLine(self.line, self.left, self.num)
        self.result = set_result(self.size, self.reline)

    @classmethod
    def tearDown(self):
        pass

    def test_find_hash(self):
        self.assertEqual(find_hash(self.line), 1, msg="#이 없는 문장")

    def test_find_left(self):
        self.assertEqual(find_left(self.line),0, msg="#의 위치를 찾을 수 없는 문장")

    def test_find_len(self):
        self.assertEqual(find_len(self.line),5)
    
    def test_set_hashLine(self):
        self.assertEqual(set_hashLine(self.line, self.left, self.num),'#', msg="#으로 이루어진 부분이 없음")

    def test_set_strLine(self):
        self.assertEqual(set_strLine(self.line, self.num, self.left, self.right),' 줄째첫')

    def test_revers_str(self):
        only_str = '줄째첫'
        self.assertEqual(revers_str(only_str),'첫째줄')

    def test_set_result(self):
        self.assertEqual(set_result(self.size, self.reline),'# 첫째줄', msg="#이 없기 때문에 '# 첫째줄'과 같지 않음")

    def test_write_result(self):
        write_result(self.re_path, self.result)
        with open(self.re_path, 'rt', encoding='UTF-8')as r:
            confirm_line = r.read()
        self.assertEqual(confirm_line, '# 첫째줄', msg="예상한 결과값(# 첫째줄)과 같이 않음")

    def test_revers_string(self):
        revers_string(self.src_path,self.re_path)
        with open(self.re_path, 'rt', encoding='UTF-8')as r:
            confirm_line = r.read()
        self.assertEqual(confirm_line, '# 첫째줄 ', msg="예상한 결과값(# 첫째줄)과 같이 않음")


if __name__ == "__main__":
    unittest.main()
