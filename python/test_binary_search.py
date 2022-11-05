import unittest
from binary_search import *
from nose.tools import eq_

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.data = [1, 3, 4, 13, 40, 193]
        self.data2 = [-1, 10, 29, 67, 998]
        self.data3 = [1, 1, 1]

    def test_binary_search(self):
        eq_(binary_search(self.data, 40), 4)
        eq_(binary_search(self.data, 1), 0)
        eq_(binary_search(self.data, 5), -1)
        eq_(binary_search(self.data, 76), -1)
        eq_(binary_search(self.data, 1000), -1)
        eq_(binary_search(self.data, 0), -1)

        eq_(binary_search(self.data3, 1), 1)
        eq_(binary_search(self.data3, 2), -1)


if __name__ == "__main__":
    unittest.main()
