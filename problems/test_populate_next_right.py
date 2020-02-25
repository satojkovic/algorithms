import unittest
from populate_next_right import *
from nose.tools import eq_

class TestPopulateNextRight(unittest.TestCase):
    def test_populate_next_right(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        new_root = populate_next_right(root)
        eq_(new_root.next, None)
        eq_(new_root.left.next, new_root.right)
        eq_(new_root.right.next, None)
        eq_(new_root.left.left.next, new_root.left.right)
        eq_(new_root.left.right.next, new_root.right.left)
        eq_(new_root.right.left.next, new_root.right.right)
        eq_(new_root.right.right.next, None)

if __name__ == "__main__":
    unittest.main()