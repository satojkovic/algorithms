import unittest
from dominant_index import *
from nose.tools import eq_

class TestDominantIndex(unittest.TestCase):
    def test_dominant_index(self):
        eq_(dominant_index([3, 2, 10, 4, 5]), 2)
        eq_(dominant_index([1]), 0)
        eq_(dominant_index([2, 2, 2, 2]), -1)
        eq_(dominant_index([1, 2, 3]), -1)

if __name__ == "__main__":
    unittest.main()