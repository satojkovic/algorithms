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

    def test_search(self):
        eq_(search(self.root, 6), True)
        eq_(search(self.root, 8), True)
        eq_(search(self.root, 20), True)
        eq_(search(self.root, 4), True)
        eq_(search(self.root, 10), True)
        eq_(search(self.root, 0), False)
        eq_(search(self.root, 1230), False)
        eq_(search(self.root, None), False)

if __name__ == "__main__":
    unittest.main()