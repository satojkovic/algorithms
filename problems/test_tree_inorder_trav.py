import unittest
from tree_inorder_trav import *
from nose.tools import eq_

class TestTreeInorderTrav(unittest.TestCase):
    def setUp(self):
        self.root = TreeNode(1)
        self.root.right = TreeNode(2)
        self.root.right.left = TreeNode(3)

        self.root_b = TreeNode(10)

        self.root_c = TreeNode(100)
        self.root_c.left = TreeNode(12)
        self.root_c.left.left = TreeNode(987)

        self.root_d = None

    def test_tree_inorder_trav1(self):
        eq_(tree_inorder_trav1(self.root), [1, 3, 2])
        eq_(tree_inorder_trav1(self.root_b), [10])
        eq_(tree_inorder_trav1(self.root_c), [987, 12, 100])
        eq_(tree_inorder_trav1(self.root_d), [])

    def test_tree_inorder_trav2(self):
        eq_(tree_inorder_trav2(self.root), [1, 3, 2])
        eq_(tree_inorder_trav2(self.root_b), [10])
        eq_(tree_inorder_trav2(self.root_c), [987, 12, 100])
        eq_(tree_inorder_trav2(self.root_d), [])

if __name__ == "__main__":
    unittest.main()