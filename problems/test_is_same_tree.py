import unittest
from is_same_tree import *
from nose.tools import eq_

class TestIsSameTree(unittest.TestCase):
    def test_is_same_tree(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        eq_(is_same_tree(p, q), True)

        p = TreeNode(1)
        p.right = TreeNode(2)
        q = TreeNode(1)
        q.left = TreeNode(2)
        eq_(is_same_tree(p, q), False)

        p = TreeNode(1)
        q = TreeNode(2)
        eq_(is_same_tree(p, q), False)

        p = None
        q = None
        eq_(is_same_tree(p, q), True)

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.left.left = TreeNode(3)
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.left.left = TreeNode(3)
        eq_(is_same_tree(p, q), True)

if __name__ == "__main__":
    unittest.main()
