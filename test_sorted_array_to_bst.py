import unittest
from sorted_array_to_bst import *
from nose.tools import eq_

class TestSortedArrayToBST(unittest.TestCase):
    def test_sorted_array_to_bst1(self):
        root = sorted_array_to_bst1([-20, -10, -3, 0, 5, 9, 11])
        eq_(root.val, 0)
        eq_(root.left.val, -10)
        eq_(root.right.val, 9)
        eq_(root.left.left.val, -20)
        eq_(root.left.right.val, -3)
        eq_(root.right.left.val, 5)
        eq_(root.right.right.val, 11)

        root = sorted_array_to_bst1([])
        eq_(root, None)

        root = sorted_array_to_bst1([-1, 4])
        eq_(root.val, 4)
        eq_(root.left.val, -1)
        eq_(root.right, None)

        root = sorted_array_to_bst1([100])
        eq_(root.val, 100)
        eq_(root.left, None)
        eq_(root.right, None)

if __name__ == "__main__":
    unittest.main()
