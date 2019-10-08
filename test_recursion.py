import unittest
from recursion import *
from nose.tools import eq_

class TestRecursion(unittest.TestCase):
    def test_fib(self):
        eq_(fib(0), 0)
        eq_(fib(1), 1)
        eq_(fib(10), 55)

if __name__ == "__main__":
    unittest.main()