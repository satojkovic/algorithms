import unittest
from right_side_view import *
from nose.tools import eq_

class TestRightSideView(unittest.TestCase):
    def test_right_side_view(self):
        root = TreeNode(4)
        root.left = TreeNode(3)
        root.right = TreeNode(8)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(9)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        eq_(right_side_view(root), [4, 8, 7])

if __name__ == "__main__":
    unittest.main()