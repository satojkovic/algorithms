#!/usr/bin/env python
# -*- coding=utf-8 -*-

class BinaryTrieNode:
    def __init__(self):
        self.zero = None
        self.one = None

class BinaryTrie:
    def __init__(self, length=3):
        self.root = BinaryTrieNode()
        self.length = length

    def insert(self, num):
        node = self.root
        for i in range(self.length - 1, -1, -1):
            cur_bit = (num >> i) & 1
            if cur_bit:
                if not node.one:
                    node.one = BinaryTrieNode()
                node = node.one
            else:
                if not node.zero:
                    node.zero = BinaryTrieNode()
                node = node.zero