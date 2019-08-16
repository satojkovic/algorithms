import unittest
from title_to_number import *
from nose.tools import eq_

class TestTitleToNumber(unittest.TestCase):
    def test_title_to_number1(self):
        eq_(title_to_number1('ZY'), 701)
        eq_(title_to_number1('A'), 1)
        eq_(title_to_number1(''), 0)
        eq_(title_to_number1('zy'), 701)
        eq_(title_to_number1('zY'), 701)
        eq_(title_to_number1('Zy'), 701)

if __name__ == "__main__":
    unittest.main()