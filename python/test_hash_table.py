from hash_table import *
import unittest
from nose.tools import ok_, eq_

class TestHashTable(unittest.TestCase):
    def test_put_get(self):
        ht = HashTable()
        ht.put(1, 1)
        ht.put(2, 2)
        ht.put(10, 10)
        ht.put(20, 20)
        ht.put(1000, 1000)
        eq_(ht.size, 5)
        eq_(ht.get(1), 1)
        eq_(ht.get(3), -1)
        eq_(ht.get(10), 10)
        eq_(ht.get(20), 20)
        eq_(ht.get(1000), 1000)
        eq_(ht.get(10000), -1)
        eq_(ht.get('a'), -1)

    def test_remove(self):
        ht = HashTable()
        ht.put(1, 1)
        ht.put(2, 2)
        eq_(ht.size, 2)
        ht.put(2, 1)
        eq_(ht.size, 2)
        eq_(ht.remove(2), True)
        eq_(ht.size, 1)
        eq_(ht.get(2), -1)
        eq_(ht.remove(1), True)
        eq_(ht.size, 0)
        eq_(ht.get(1), -1)
        eq_(ht.remove(1), False)


if __name__ == "__main__":
    unittest.main()