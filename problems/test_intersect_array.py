import unittest
from intersect_array import *
from nose.tools import eq_

class TestIntersectArray(unittest.TestCase):
    def test_intersect1(self):
        eq_(intersect1([9, 4, 9, 8, 4], [4, 9, 5]), [4, 9])
        eq_(intersect1([], [1, 2, 3]), [])
        eq_(intersect1([10, 20, 30], []), [])
        eq_(intersect1([], []), [])

if __name__ == "__main__":
    unittest.main()