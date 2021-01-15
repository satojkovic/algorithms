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

        self.root2 = None

    def test_inorder(self):
        eq_(inorder(self.root), [2, 4, 6, 8, 10, 20])
        eq_(inorder(self.root2), [])

    def test_inorder_iter(self):
        res = inorder_iter(self.root)
        eq_(res, [2, 4, 6, 8, 10, 20])

    def test_preorder(self):
        eq_(preorder(self.root), [8, 4, 2, 6, 10, 20])
        eq_(preorder(self.root2), [])

    def test_preorder_iter(self):
        eq_(preorder_iter(self.root), [8, 4, 2, 6, 10, 20])
        eq_(preorder_iter(self.root2), [])

    def test_postorder_retlist(self):
        eq_(postorder_retlist(self.root), [2, 6, 4, 20, 10, 8])
        eq_(postorder_retlist(self.root2), [])

    def test_levelorder(self):
        eq_(levelorder(self.root), [[8], [4, 10], [2, 6, 20]])

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.left.left = TreeNode(5)
        eq_(levelorder(root), [[1], [2], [3], [4], [5]])

        root = None
        eq_(levelorder(root), [])

if __name__ == "__main__":
    unittest.main()