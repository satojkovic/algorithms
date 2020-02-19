import unittest
from valid_bst import *
from nose.tools import eq_

class TestValidBst(unittest.TestCase):
    def test_valid_bst(self):
        root = TreeNode(8)
        root.left = TreeNode(4)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(6)
        root.right = TreeNode(9)
        eq_(validate_bst(root), True)

        root.left.right = TreeNode(9)
        eq_(validate_bst(root), False)

if __name__ == "__main__":
    unittest.main()