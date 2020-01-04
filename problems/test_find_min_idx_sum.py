import unittest
from find_min_idx_sum import *
from nose.tools import eq_

class TestFindMinIdxSum(unittest.TestCase):
    def test_find_min_idx_sum(self):
        eq_(find_min_idx_sum(['a', 'b', 'c'], ['d', 'e', 'c', 'a', 'f', 'b']), ['a'])
        eq_(find_min_idx_sum(['a', 'b', 'c'], ['c']), ['c'])
        eq_(find_min_idx_sum(['b', 'f'], ['f', 'b']), ['b', 'f'])
        eq_(find_min_idx_sum(['a'], ['a']), ['a'])

if __name__ == "__main__":
    unittest.main()