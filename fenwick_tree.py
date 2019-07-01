#!/usr/bin/env python
# -*- coding=utf-8 -*-

class FenwickTree:
    def __init__(self, size):
        # Create an empty FenwickTree
        self.tree = [0 for _ in range(size + 1)]

    def construct(self, values):
        if len(values) == 0:
            return None
        self.tree[1:] = values
        for i in range(1, len(self.tree)):
            j = i + self._lsb(i)
            if j < len(self.tree):
                self.tree[j] += self.tree[i]

    def _lsb(self, i):
        return i & -i
