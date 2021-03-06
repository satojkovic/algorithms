import unittest
from binary_search_tree import *
from nose.tools import eq_

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.root = TreeNode(8)
        self.root.left = TreeNode(4)
        self.root.left.left = TreeNode(2)
        self.root.left.right = TreeNode(6)
        self.root.right = TreeNode(10)
        self.root.right.right = TreeNode(20)

        self.root2 = TreeNode(8)
        self.root2.left = TreeNode(4)
        self.root2.left.left = TreeNode(2)
        self.root2.left.right = TreeNode(9)
        self.root2.right = TreeNode(10)
        self.root2.right.right = TreeNode(20)

        self.root3 = TreeNode(3)
        self.root3.right = TreeNode(30)
        self.root3.right.left = TreeNode(10)
        self.root3.right.left.right = TreeNode(15)
        self.root3.right.left.right.right = TreeNode(45)

    def test_search(self):
        eq_(search(self.root, 6), True)
        eq_(search(self.root, 8), True)
        eq_(search(self.root, 20), True)
        eq_(search(self.root, 4), True)
        eq_(search(self.root, 10), True)
        eq_(search(self.root, 0), False)
        eq_(search(self.root, 1230), False)
        eq_(search(self.root, None), False)

    def test_add(self):
        root = add(None, 8)
        root = add(root, 4)
        root = add(root, 2)
        root = add(root, 6)
        root = add(root, 10)
        root = add(root, 20)

        eq_(root.data, 8)
        eq_(root.left.data, 4)
        eq_(root.left.left.data, 2)
        eq_(root.left.right.data, 6)
        eq_(root.right.data, 10)
        eq_(root.right.right.data, 20)

if __name__ == "__main__":
    unittest.main()