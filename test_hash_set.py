import unittest
from hash_set import *
from nose.tools import eq_

class TestHashSet(unittest.TestCase):
    def test_add(self):
        hs = HashSet(3)
        hs.add(1)
        hs.add(2)
        hs.add(3)
        eq_(hs.data[1], 1)
        eq_(hs.data[2], 2)
        eq_(hs.data[0], 3)

if __name__ == "__main__":
    unittest.main()