import unittest
from find_dups import *
from nose.tools import eq_

class TestFindDups(unittest.TestCase):
    def test_find_dups1(self):
        eq_(find_dups1([1, 2, 3, 1]), True)
        eq_(find_dups1([1, 2, 3, 4]), False)
        eq_(find_dups1([1]), False)

    def test_find_dups2(self):
        eq_(find_dups2([1, 2, 3, 1]), True)
        eq_(find_dups2([1, 2, 3, 4]), False)
        eq_(find_dups2([1]), False)

if __name__ == "__main__":
    unittest.main()