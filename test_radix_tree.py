#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
import radix_tree
from nose.tools import eq_

class TestRadixTree(unittest.TestCase):
    def setUp(self):
        self.rtree = radix_tree.RadixTree()

    def test_insert(self):
        self.rtree.insert(0)
        eq_(self.rtree.root.zero.zero.zero.zero, None)
        eq_(self.rtree.root.zero.zero.zero.one, None)

        self.rtree.insert(4)
        eq_(self.rtree.root.one.zero.zero.zero, None)
        eq_(self.rtree.root.one.zero.zero.one, None)

    def test_prefix_search(self):
        self.rtree.insert(0)
        self.rtree.insert(4)
        eq_(self.rtree.prefix_search(0), True)
        eq_(self.rtree.prefix_search(4), True)
        eq_(self.rtree.prefix_search(5), False)


if __name__ == "__main__":
    unittest.main()