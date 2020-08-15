import unittest
from max_subarray import *
from nose.tools import eq_

class TestMaxSubarray(unittest.TestCase):
    def test_max_subarray1(self):
        eq_(max_subarray1([-2,1,-3,4,-1,2,1,-5,4]), 6)
        eq_(max_subarray1([10]), 10)
        eq_(max_subarray2([-1, -1, -2, 100]), 100)
        eq_(max_subarray2([543, -10, -25, -100]), 543)
        eq_(max_subarray1([]), None)

    def test_max_subarray2(self):
        eq_(max_subarray2([-2,1,-3,4,-1,2,1,-5,4]), 6)
        eq_(max_subarray2([10]), 10)
        eq_(max_subarray2([-1, -1, -2, 100]), 100)
        eq_(max_subarray2([543, -10, -25, -100]), 543)
        eq_(max_subarray2([]), None)

    def test_max_subarray3(self):
        eq_(max_subarray3([-2,1,-3,4,-1,2,1,-5,4]), 6)
        eq_(max_subarray3([10]), 10)
        eq_(max_subarray3([-1, -1, -2, 100]), 100)
        eq_(max_subarray3([543, -10, -25, -100]), 543)
        eq_(max_subarray3([]), None)

if __name__ == "__main__":
    unittest.main()