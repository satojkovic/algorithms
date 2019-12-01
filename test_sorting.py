import unittest
from merge_sort import *
from quick_sort import *
from nose.tools import eq_

class TestSort(unittest.TestCase):
    def test_merge_sort(self):
        eq_(merge_sort([1, 5, 3, 2, 8, 7, 6, 4]), [1, 2, 3, 4, 5, 6, 7, 8])
        eq_(merge_sort([100, 3, 9]), [3, 9, 100])
        eq_(merge_sort([]), [])
        eq_(merge_sort([123]), [123])
        eq_(merge_sort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_quick_sort(self):
        eq_(quick_sort([1, 5, 8, 2, 3, 7, 6, 4]), [1, 2, 3, 4, 5, 6, 7, 8])
        eq_(quick_sort([100, 3, 9]), [3, 9, 100])
        eq_(quick_sort([]), [])
        eq_(quick_sort([123]), [123])
        eq_(quick_sort([1, 1, 1, 1]), [1, 1, 1, 1])

if __name__ == "__main__":
    unittest.main()