import unittest
from sum_two_int import *
from nose.tools import eq_
import sys

class TestSumTwoInt(unittest.TestCase):
    def test_sum_two_int1(self):
        eq_(sum_two_int1(1, 2), 3)
        eq_(sum_two_int1(0, 4), 4)
        eq_(sum_two_int1(12, 0), 12)
        eq_(sum_two_int1(0, 0), 0)
        eq_(sum_two_int1(-1, 3), 2)
        eq_(sum_two_int1(-18, -125), -143)

if __name__ == "__main__":
    unittest.main()