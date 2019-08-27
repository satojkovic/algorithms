import unittest
from is_symmetry import *
from nose.tools import eq_

class TestIsSymmetry(unittest.TestCase):
    def setUp(self):
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(2)

    def test_is_symmetry1(self):
        eq_(is_symmetry1(self.root), True)


if __name__ == "__main__":
    unittest.main()