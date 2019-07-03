import hash_table
import unittest
from nose.tools import ok_, eq_

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = hash_table.HashTable()

    def test_empty(self):
        eq_(self.ht.is_empty(), True)
        self.ht.insert('test', 1)
        eq_(self.ht.is_empty(), False)

    def test_insert(self):
        self.ht.insert('test', 1)
        eq_(self.ht.get('test'), 1)

        self.ht.insert('hash', 10)
        eq_(self.ht.get('hash'), 10)

        self.ht.insert('test', 100)
        eq_(self.ht.get('test'), 100)

    def test_resize(self):
        eq_(self.ht.capacity, 3)
        for i in range(3):
            key = str(i)
            self.ht.insert('test' + key, i)
        eq_(self.ht.capacity, 6)
        for i in range(3):
            key = str(i + 3)
            self.ht.insert('test' + key, i)
        eq_(self.ht.capacity, 12)

if __name__ == "__main__":
    unittest.main()