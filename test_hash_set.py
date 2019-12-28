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

if __name__ == "__main__":
    unittest.main()