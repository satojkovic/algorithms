import unittest
import fenwick_tree
from nose.tools import ok_, eq_

class TestFenwickTree(unittest.TestCase):
    def setUp(self):
        self.ft = fenwick_tree.FenwickTree(12)

    def test_construct(self):
        values = [3, 4, -2, 7, 3, 11, 5, -8, -9, 2, 4, -8]
        self.ft.construct(values)
        eq_(self.ft.tree[1:], [3, 7, -2, 12, 3, 14, 5, 23, -9, -7, 4, -11])

if __name__ == "__main__":
    unittest.main()
