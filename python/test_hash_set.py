import unittest
from hash_set import *
from nose.tools import eq_

class TestHashSet(unittest.TestCase):
    def test_add(self):
        hs = HashSet(3)
        hs.add(1)
        hs.add(2)
        eq_(hs.contains(1), True)
        eq_(hs.contains(2), True)
        eq_(hs.contains(3), False)

        hs.add(10)
        hs.add(20)
        hs.add(30)
        eq_(hs.contains(10), True)
        eq_(hs.contains(20), True)
        eq_(hs.contains(30), True)

    def test_remove(self):
        hs = HashSet(3)
        hs.add(1)
        hs.add(2)
        eq_(hs.contains(1), True)
        eq_(hs.contains(3), False)
        eq_(hs.remove(1), 1)
        eq_(hs.contains(2), True)

if __name__ == "__main__":
    unittest.main()