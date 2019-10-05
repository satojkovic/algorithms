import unittest
from tree_traversals import *
from nose.tools import eq_

class TestTreeTraversals(unittest.TestCase):
    def setUp(self):
        self.root = TreeNode(8)
        self.root.left = TreeNode(4)
        self.root.left.left = TreeNode(2)
        self.root.left.right = TreeNode(6)
        self.root.right = TreeNode(10)
        self.root.right.right = TreeNode(20)

    def test_inorder_retlist(self):
        eq_(inorder_retlist(self.root), [2, 4, 6, 8, 10, 20])

    def test_inorder_retlist2(self):
        eq_(inorder_retlist2(self.root), [2, 4, 6, 8, 10, 20])

    def test_preorder_retlist(self):
        eq_(preorder_relist(self.root), [8, 4, 2, 6, 10, 20])

    def test_postorder_retlist(self):
        eq_(postorder_retlist(self.root), [2, 6, 4, 20, 10, 8])

if __name__ == "__main__":
    unittest.main()