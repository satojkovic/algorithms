#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
from avl_tree import *
from nose.tools import eq_, ok_

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.avl_tree = AVLTree()

    def test_init(self):
        eq_(self.avl_tree.root, None)
        eq_(self.avl_tree.node_count, 0)
        eq_(self.avl_tree.insert(None), False)

    def test_leftleft_case(self):
        self.avl_tree.insert(3)
        self.avl_tree.insert(2)
        self.avl_tree.insert(1)

        eq_(self.avl_tree.root.value, 2)
        eq_(self.avl_tree.root.left.value, 1)
        eq_(self.avl_tree.root.right.value, 3)

        eq_(self.avl_tree.root.left.left, None)
        eq_(self.avl_tree.root.left.right, None)
        eq_(self.avl_tree.root.right.left, None)
        eq_(self.avl_tree.root.right.right, None)

    def test_leftright_case(self):
        self.avl_tree.insert(3)
        self.avl_tree.insert(1)
        self.avl_tree.insert(2)

        eq_(self.avl_tree.root.value, 2)
        eq_(self.avl_tree.root.left.value, 1)
        eq_(self.avl_tree.root.right.value, 3)

        eq_(self.avl_tree.root.left.left, None)
        eq_(self.avl_tree.root.left.right, None)
        eq_(self.avl_tree.root.right.left, None)
        eq_(self.avl_tree.root.right.right, None)

    def test_rightright_case(self):
        self.avl_tree.insert(1)
        self.avl_tree.insert(2)
        self.avl_tree.insert(3)

        eq_(self.avl_tree.root.value, 2)
        eq_(self.avl_tree.root.left.value, 1)
        eq_(self.avl_tree.root.right.value, 3)

        eq_(self.avl_tree.root.left.left, None)
        eq_(self.avl_tree.root.left.right, None)
        eq_(self.avl_tree.root.right.left, None)
        eq_(self.avl_tree.root.right.right, None)

    def test_rightleft_case(self):
        self.avl_tree.insert(1)
        self.avl_tree.insert(3)
        self.avl_tree.insert(2)

        eq_(self.avl_tree.root.value, 2)
        eq_(self.avl_tree.root.left.value, 1)
        eq_(self.avl_tree.root.right.value, 3)

        eq_(self.avl_tree.root.left.left, None)
        eq_(self.avl_tree.root.left.right, None)
        eq_(self.avl_tree.root.right.left, None)
        eq_(self.avl_tree.root.right.right, None)

if __name__ == "__main__":
    unittest.main()