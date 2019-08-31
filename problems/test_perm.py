import unittest
from perm import *
from nose.tools import eq_

class TestPerm(unittest.TestCase):
    def test_perm1(self):
        eq_(perm1([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
        eq_(perm1([]), [[]])
        eq_(perm1([100]), [[100]])
        eq_(perm1([456, 456]), [[456, 456], [456, 456]])

if __name__ == "__main__":
    unittest.main()