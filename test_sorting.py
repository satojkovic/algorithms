import unittest
from merge_sort import *
from nose.tools import eq_

class TestSort(unittest.TestCase):
    def test_merge_sort(self):
        eq_(merge_sort([1, 5, 3, 2, 8, 7, 6, 4]), [1, 2, 3, 4, 5, 6, 7, 8])
        eq_(merge_sort([100, 3, 9]), [3, 9, 100])
        eq_(merge_sort([]), [])
        eq_(merge_sort([123]), [123])

if __name__ == "__main__":
    unittest.main()