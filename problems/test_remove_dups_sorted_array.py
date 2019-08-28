import unittest
from remove_dups import *
from nose.tools import eq_

class TestRemoveDups(unittest.TestCase):
    def test_remove_dups1(self):
        eq_(remove_dups1([1, 1, 2]), 2)
        eq_(remove_dups1([0,0,1,1,1,2,2,3,3,4]), 5)
        eq_(remove_dups1([10]), 1)
        eq_(remove_dups1([]), 0)
        eq_(remove_dups1([11, 12, 13, 14]), 4)

if __name__ == "__main__":
    unittest.main()