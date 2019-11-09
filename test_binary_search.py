import unittest
from binary_search import *
from nose.tools import eq_

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.data = [1, 3, 4, 13, 40, 193]
        self.data2 = [-1, 10, 29, 67, 998]
        self.data3 = [1, 1, 1]

    def test_binary_search_r(self):
        eq_(binary_search_r(self.data, 40, 0, len(self.data) - 1), True)
        eq_(binary_search_r(self.data, 1, 0, len(self.data) - 1), True)
        eq_(binary_search_r(self.data, 5, 0, len(self.data) - 1), False)
        eq_(binary_search_r(self.data, 76, 0, len(self.data) - 1), False)        
        eq_(binary_search_r(self.data, 1000, 0, len(self.data) - 1), False)
        eq_(binary_search_r(self.data, 0, 0, len(self.data) - 1), False)

        eq_(binary_search_r(self.data2, -1, 0, len(self.data2) - 1), True)

        eq_(binary_search_r(self.data3, 1, 0, len(self.data3) - 1), True)
        eq_(binary_search_r(self.data3, 2, 0, len(self.data3) - 1), False)

    def test_search_2d_mat(self):
        mat = [
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        eq_(search_2d_mat(mat, 5), True)
        eq_(search_2d_mat(mat, 20), False)

if __name__ == "__main__":
    unittest.main()