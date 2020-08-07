import unittest
from largest_island import *
from nose.tools import eq_

class TestLargestIsland(unittest.TestCase):
    def test_largest_island(self):
        mat = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]
        ]
        eq_(largest_island(mat), 5)

if __name__ == "__main__":
    unittest.main()
