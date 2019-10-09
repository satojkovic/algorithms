import unittest
from recursion import *
from nose.tools import eq_

class TestRecursion(unittest.TestCase):
    def test_fib(self):
        eq_(fib(0), 0)
        eq_(fib(1), 1)
        eq_(fib(10), 55)

    def test_reverse_str(self):
        eq_(reverse_str('abcde'), 'edcba')
        eq_(reverse_str('A'), 'A')
        eq_(reverse_str(''), '')
        eq_(reverse_str('AB'), 'BA')

if __name__ == "__main__":
    unittest.main()