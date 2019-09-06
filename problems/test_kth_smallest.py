import unittest
from kth_smallest import TreeNode, kth_smallest1, kth_smallest2
from nose.tools import eq_

class TestKthSmallest(unittest.TestCase):
    def setUp(self):
        self.root1 = TreeNode(3)
        self.root1.left = TreeNode(1)
        self.root1.right = TreeNode(4)
        self.root1.left.right = TreeNode(2)

    def test_kth_smallest1(self):
        eq_(kth_smallest1(self.root1, 1), 1)
        eq_(kth_smallest1(self.root1, 4), 4)

    def test_kth_smallest2(self):
        eq_(kth_smallest2(self.root1, 1), 1)
        eq_(kth_smallest2(self.root1, 4), 4)

if __name__ == "__main__":
    unittest.main()