from hash_table import *
import unittest
from nose.tools import ok_, eq_

class TestHashTable(unittest.TestCase):
    def test_put_get(self):
        ht = HashTable()
        ht.add(1, 1)
        ht.add(2, 2)
        ht.add(10, 10)
        ht.add(20, 20)
        ht.add(1000, 1000)
        eq_(ht.size, 5)
        eq_(ht.get(1), 1)
        eq_(ht.get(3), None)
        eq_(ht.get(10), 10)
        eq_(ht.get(20), 20)
        eq_(ht.get(1000), 1000)
        eq_(ht.get(10000), None)
        eq_(ht.get('a'), None)

    def test_remove(self):
        ht = HashTable()
        ht.add(1, 1)
        ht.add(2, 2)
        eq_(ht.size, 2)
        ht.add(2, 1)
        eq_(ht.size, 2)
        eq_(ht.remove(2), 2)
        eq_(ht.size, 1)
        eq_(ht.get(2), None)
        eq_(ht.remove(1), 1)
        eq_(ht.size, 0)
        eq_(ht.get(1), None)
        eq_(ht.remove(1), None)


if __name__ == "__main__":
    unittest.main()