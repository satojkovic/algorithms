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

    def add(self, i, k):
        if i == 0:
            return False
        while i < len(self.tree):
            self.tree[i] += k
            i += self._lsb(i)

    def _lsb(self, i):
        return i & -i
