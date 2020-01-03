import unittest
from is_isomorphic import *
from nose.tools import eq_

class TestIsIsomorphic(unittest.TestCase):
    def test_is_isomorphic(self):
        eq_(is_isomorphic('add', 'egg'), True)
        eq_(is_isomorphic('fore', 'bare'), True)
        eq_(is_isomorphic('ab', 'aa'), False)
        eq_(is_isomorphic('akb', 'bkb'), False)
        eq_(is_isomorphic('a', 'a'), True)
        eq_(is_isomorphic('ccc', 'aaa'), True)
        eq_(is_isomorphic('', ''), True)

if __name__ == "__main__":
    unittest.main()