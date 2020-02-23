import unittest
from inorder_successor import *
from nose.tools import eq_

class TestInorderSuccessor(unittest.TestCase):
    def test_inorder_successor(self):
        root = TreeNode(10)
        left = TreeNode(5)
        right = TreeNode(20)
        left_left = TreeNode(2)
        left_right = TreeNode(9)
        root.left = left
        root.right = right
        left.left = left_left
        left.right = left_right

        s = inorder_successor(root, left_left)
        eq_(s.val, left.val)

        s = inorder_successor(root, right)
        eq_(s, None)

        s = inorder_successor(root, left_right)
        eq_(s.val, root.val)

        s = inorder_successor(None, None)
        eq_(s, None)

    def test_inorder_successor_iter(self):
        root = TreeNode(10)
        left = TreeNode(5)
        right = TreeNode(20)
        left_left = TreeNode(2)
        left_right = TreeNode(9)
        root.left = left
        root.right = right
        left.left = left_left
        left.right = left_right

        s = inorder_successor_iter(root, left_left)
        eq_(s.val, left.val)

        s = inorder_successor_iter(root, right)
        eq_(s, None)

        s = inorder_successor_iter(root, left_right)
        eq_(s.val, root.val)

        s = inorder_successor_iter(None, None)
        eq_(s, None)

if __name__ == "__main__":
    unittest.main()