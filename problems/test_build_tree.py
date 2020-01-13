import unittest
from build_tree import *
from nose.tools import eq_

class TestBuildTree(unittest.TestCase):
    def test_build_tree(self):
        root = build_tree([9, 8, 3, 15, 20, 7], [8, 9, 15, 7, 20, 3])
        eq_(root.val, 3)
        eq_(root.left.val, 9)
        eq_(root.right.val, 20)
        eq_(root.left.right.val, 8)
        eq_(root.right.left.val, 15)
        eq_(root.right.right.val, 7)

    def test_build_tree2(self):
        root = build_tree2([9, 8, 3, 15, 20, 7], [8, 9, 15, 7, 20, 3])
        eq_(root.val, 3)
        eq_(root.left.val, 9)
        eq_(root.right.val, 20)
        eq_(root.left.right.val, 8)
        eq_(root.right.left.val, 15)
        eq_(root.right.right.val, 7)

    def test_build_tree_pre_in(self):
        root = build_tree_pre_in([3, 9, 8, 20, 15, 7], [9, 8, 3, 15, 20, 7])
        eq_(root.val, 3)
        eq_(root.left.val, 9)
        eq_(root.right.val, 20)
        eq_(root.left.right.val, 8)
        eq_(root.right.left.val, 15)
        eq_(root.right.right.val, 7)

if __name__ == "__main__":
    unittest.main()