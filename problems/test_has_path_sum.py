import unittest
from has_path_sum import *
from nose.tools import eq_

class TestHasPathSum(unittest.TestCase):
    def test_has_path_sum(self):
        eq_(has_path_sum(None, 10), False)

        root = TreeNode(1)
        root.left = TreeNode(2)
        eq_(has_path_sum(root, 1), False)

        root = TreeNode(1)
        eq_(has_path_sum(root, 1), True)

        root = TreeNode(10)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(-5)
        eq_(has_path_sum(root, 12), True)
        eq_(has_path_sum(root, 8), True)
        eq_(has_path_sum(root, 100), False)

if __name__ == "__main__":
    unittest.main()