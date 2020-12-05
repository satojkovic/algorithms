#!/usr/bin/env python
# -*- coding=utf-8 -*-

class RadixTreeNode:
    def __init__(self):
        self.zero = None
        self.one = None

class RadixTree:
    def __init__(self, length=3):
        self.root = RadixTreeNode()
        self.length = length

    def insert(self, num):
        node = self.root
        for i in range(self.length - 1, -1, -1):
            cur_bit = (num >> i) & 1
            if cur_bit:
                if not node.one:
                    node.one = RadixTreeNode()
                node = node.one
            else:
                if not node.zero:
                    node.zero = RadixTreeNode()
                node = node.zero

    def prefix_search(self, num):
        node = self.root
        for i in range(self.length - 1, -1, -1):
            cur_bit = (num >> i) & 1
            if cur_bit:
                if not node.one:
                    return False
                node = node.one
            else:
                if not node.zero:
                    return False
                node = node.zero
        return True
