import unittest
from plus_one import *
from nose.tools import eq_

class TestPlusOne(unittest.TestCase):
    def test_plus_one(self):
        eq_(plus_one([1, 2, 3]), [1, 2, 4])
        eq_(plus_one([5, 6, 7, 8]), [5, 6, 7, 9])
        eq_(plus_one([0]), [1])
        eq_(plus_one([9]), [1, 0])
        eq_(plus_one([9, 9, 9]), [1, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()