import unittest
from intersect_array import *
from nose.tools import eq_

class TestIntersectArray(unittest.TestCase):
    def test_intersect1(self):
        eq_(intersect1([9, 4, 9, 8, 4], [4, 9, 5]), [4, 9])
        eq_(intersect1([], [1, 2, 3]), [])
        eq_(intersect1([10, 20, 30], []), [])
        eq_(intersect1([], []), [])

    def test_intersect2(self):
        eq_(intersect2([9, 4, 9, 8, 4], [4, 9, 5]), [9, 4])
        eq_(intersect2([], [1, 2, 3]), [])
        eq_(intersect2([10, 20, 30], []), [])
        eq_(intersect2([], []), [])

    def test_intersect3(self):
        eq_(intersect3([4, 4, 8, 9, 9], [4, 5, 9]), [4, 9])
        eq_(intersect3([], [1, 2, 3]), [])
        eq_(intersect3([10, 20, 30], []), [])
        eq_(intersect3([], []), [])

if __name__ == "__main__":
    unittest.main()