import unittest
from max_depth import max_depth, TreeNode
from nose.tools import eq_, ok_

class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        self.root = TreeNode(3)
        self.root.left = TreeNode(9)
        self.root.right = TreeNode(20)
        self.root.right.left = TreeNode(15)
        self.root.right.right = TreeNode(7)

    def test_max_depth(self):
        eq_(max_depth(self.root), 3)

if __name__ == "__main__":
    unittest.main()