import unittest
from merge_sort import *
from sorting import quick_sort, quick_sort_in_place, insertion_sort
from nose.tools import eq_

class TestSort(unittest.TestCase):
    def test_insertion_sort(self):
        eq_(insertion_sort([1, 5, 3, 2, 8, 7, 6, 4]), [1, 2, 3, 4, 5, 6, 7, 8])
        eq_(insertion_sort([100, 3, 9]), [3, 9, 100])
        eq_(insertion_sort([]), [])
        eq_(insertion_sort([123]), [123])
        eq_(insertion_sort([1, 1, 1, 1]), [1, 1, 1, 1])

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

    def test_quick_sort_in_place(self):
        eq_(quick_sort_in_place([1, 5, 8, 2, 3, 7, 6, 4]), [1, 2, 3, 4, 5, 6, 7, 8])
        eq_(quick_sort_in_place([100, 3, 9]), [3, 9, 100])
        eq_(quick_sort_in_place([]), [])
        eq_(quick_sort_in_place([123]), [123])
        eq_(quick_sort_in_place([1, 1, 1, 1]), [1, 1, 1, 1])

if __name__ == "__main__":
    unittest.main()