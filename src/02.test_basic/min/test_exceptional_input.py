import unittest

class test_exceptional_input(unittest.TestCase):
    def test_is_there_tag(self):
        self.assertIn(self.line, '<') #tag가 있는지 알아보는 함수, false여야 ok

    def test_is_there_golbangi(self):
        self.assertIn(self.line, '@') #@가 있는지 알아보는 함수, false여야 ok

    def test_is_there_cancleline(self):
        self.assertEqual(self.line.count('~~'), 2) #~~ ~~이 있는지 알아보는 함수

    def test_is_there_bar(self):
        self.assertIn(self.line,'---') # ---이 있는지 알아보는 함수
