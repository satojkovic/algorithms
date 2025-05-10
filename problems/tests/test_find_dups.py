import unittest
from src.find_dups import *
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

    def test_find_dups3(self):
        eq_(find_dups3([1, 3, 4, 2, 2]), 2)
        eq_(find_dups3([1, 1]), 1)
        eq_(find_dups3([3, 2, 1, 3]), 3)

if __name__ == "__main__":
    unittest.main()
