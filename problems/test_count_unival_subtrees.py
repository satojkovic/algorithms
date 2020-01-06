import unittest
from count_unival_subtrees import *
from nose.tools import eq_

class TestCountUnivalSubtrees(unittest.TestCase):
    def test_count_unival_subtrees(self):
        root = TreeNode(2)
        root.left = TreeNode(3)
        root.right = TreeNode(10)
        root.left.left = TreeNode(3)
        root.right.right = TreeNode(10)
        eq_(count_unival_subtrees(root), 4)

        root = TreeNode(1)
        eq_(count_unival_subtrees(root), 1)

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        eq_(count_unival_subtrees(root), 1)

        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        eq_(count_unival_subtrees(root), 1)

        root = TreeNode(10)
        root.left = TreeNode(10)
        root.right = TreeNode(10)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        eq_(count_unival_subtrees(root), 3)

if __name__ == "__main__":
    unittest.main()
