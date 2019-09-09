import unittest
from four_sum_count import *
from nose.tools import eq_

class TestFourSumCount(unittest.TestCase):
    def test_four_sum_count1(self):
        eq_(four_sum_count1([1, 2], [-2, -1], [-1, 2], [0, 2]), 2)
        eq_(four_sum_count1([0], [0], [0], [0]), 1)
        eq_(four_sum_count1([10], [21], [-100], [83]), 0)

if __name__ == "__main__":
    unittest.main()