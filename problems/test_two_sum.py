import unittest
from two_sum import *
from nose.tools import eq_

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        eq_(two_sum([1, 2, 7, 9], 9), [1, 2])
        eq_(two_sum([2, 2, 5, 4], 6), [1, 3])
        eq_(two_sum([1, 1, 1, 1, 1], 2), [0, 1])
        eq_(two_sum([3, 7, 11], 2), [-1, -1])
        eq_(two_sum([3, 2, 4], 6), [1, 2])

if __name__ == "__main__":
    unittest.main()