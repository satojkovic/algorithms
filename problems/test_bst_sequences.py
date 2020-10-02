import unittest
from bst_seqences import *
from nose.tools import eq_

class TestBstSequences(unittest.TestCase):
    def test_bst_sequences(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(20)
        self.assertCountEqual(bst_sequences(root), [[10, 5, 20], [10, 20, 5]])

        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.right = TreeNode(9)
        root.right.left = TreeNode(8)
        root.right.right = TreeNode(11)
        res = bst_sequences(root)
        self.assertCountEqual(res, 
            [[3, 2, 1, 9, 8, 11], [3, 2, 9, 1, 8, 11],
             [3, 2, 9, 8, 1, 11], [3, 2, 9, 8, 11, 1],
             [3, 9, 2, 1, 8, 11], [3, 9, 2, 8, 1, 11],
             [3, 9, 2, 8, 11, 1], [3, 9, 8, 2, 1, 11],
             [3, 9, 8, 2, 11, 1], [3, 9, 8, 11, 2, 1],
             [3, 2, 1, 9, 11, 8], [3, 2, 9, 1, 11, 8],
             [3, 2, 9, 11, 1, 8], [3, 2, 9, 11, 8, 1],
             [3, 9, 2, 1, 11, 8], [3, 9, 2, 11, 1, 8],
             [3, 9, 2, 11, 8, 1],
             [3, 9, 11, 2, 1, 8], [3, 9, 11, 2, 8, 1],
             [3, 9, 11, 8, 2, 1]])

        root = TreeNode(4)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right = TreeNode(5)
        root.right.right = TreeNode(6)
        res = bst_sequences(root)
        self.assertCountEqual(res,
            [[4, 2, 5, 1, 3, 6],
             [4, 2, 5, 1, 6, 3],
             [4, 2, 5, 3, 1, 6],
             [4, 2, 5, 3, 6, 1],
             [4, 2, 5, 6, 1, 3],
             [4, 2, 5, 6, 3, 1],
             [4, 2, 1, 5, 3, 6],
             [4, 2, 1, 5, 6, 3],
             [4, 2, 1, 3, 5, 6],
             [4, 2, 3, 5, 1, 6],
             [4, 2, 3, 5, 6, 1],
             [4, 2, 3, 1, 5, 6],
             [4, 5, 2, 6, 1, 3],
             [4, 5, 2, 6, 3, 1],
             [4, 5, 2, 1, 6, 3],
             [4, 5, 2, 1, 3, 6],
             [4, 5, 2, 3, 6, 1],
             [4, 5, 2, 3, 1, 6],
             [4, 5, 6, 2, 1, 3],
             [4, 5, 6, 2, 3, 1]])

if __name__ == "__main__":
    unittest.main()
