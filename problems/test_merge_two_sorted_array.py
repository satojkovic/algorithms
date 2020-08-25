import unittest
from merge_two_sorted_array import *
from nose.tools import eq_

class TestMergeTwoSortedArray(unittest.TestCase):
    def test_merge_two_sorted_list1(self):
        eq_(merge_two_sorted_array([0, 3, 4, 9, 15, 0, 0, 0, 0], [5, 7, 8, 10], 5, 4), [0, 3, 4, 5, 7, 8, 9, 10, 15])
        eq_(merge_two_sorted_array([2, 4, 15, 0, 0, 0, 0], [1, 3, 8, 28], 3, 4), [1, 2, 3, 4, 8, 15, 28])
        eq_(merge_two_sorted_array([1, 3, 4, 0, 0, 0], [0, 2, 8], 3, 3), [0, 1, 2, 3, 4, 8])
        eq_(merge_two_sorted_array([1, 1, 0, 0], [2, 2], 2, 2), [1, 1, 2, 2])

if __name__ == "__main__":
    unittest.main()