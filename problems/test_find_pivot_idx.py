import unittest
from find_pivot_idx import *
from nose.tools import eq_

class TestFindPivotIdx(unittest.TestCase):
    def test_find_pivot_idx(self):
        eq_(find_pivot_idx([1, 7, 3, 6, 5, 6]), 3)
        eq_(find_pivot_idx([1, 2, 0, 0, 3]), 2)
        eq_(find_pivot_idx([1]), 0)
        eq_(find_pivot_idx([]), -1)

if __name__ == "__main__":
    unittest.main()