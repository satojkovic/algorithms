#!/usr/bin/env python
# -*- coding=utf-8 -*-

import unittest
import trie
from nose.tools import eq_

class TestBinaryTrie(unittest.TestCase):
    def setUp(self):
        self.btrie = trie.BinaryTrie()

    def test_insert(self):
        self.btrie.insert(0)
        eq_(self.btrie.root.zero.zero.zero.zero, None)
        eq_(self.btrie.root.zero.zero.zero.one, None)

        self.btrie.insert(4)
        eq_(self.btrie.root.one.zero.zero.zero, None)
        eq_(self.btrie.root.one.zero.zero.one, None)

if __name__ == "__main__":
    unittest.main()