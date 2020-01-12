import unittest
from find_uniq_ch import *
from nose.tools import eq_

class TestFindUniqCh(unittest.TestCase):
    def test_find_uniq_ch(self):
        eq_(find_uniq_ch('abcaad'), 1)
        eq_(find_uniq_ch('a'), 0)
        eq_(find_uniq_ch(''), -1)
        eq_(find_uniq_ch('aaa'), -1)

if __name__ == "__main__":
    unittest.main()