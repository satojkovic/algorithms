import unittest
from subsets import *
from nose.tools import eq_

class TestSubsets(unittest.TestCase):
    def test_subsets1(self):
        eq_(subsets1([1, 2, 3]), [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
        eq_(subsets1([1]), [[], [1]])
        eq_(subsets1([]), [[]])
        eq_(subsets1([5, 4]), [[], [5], [5, 4], [4]])

if __name__ == "__main__":
    unittest.main()