#!/usr/bin/env python
# -*- coding=utf-8 -*-

class HashSet:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bucket = self.capacity * [None]

    def _hash(self, key):
        return hash(key) % self.capacity

    def add(self, key):
        h = self._hash(key)
        self.bucket[h] = key

    def contains(self, key):
        h = self._hash(key)
        return True if self.bucket[h] is not None else False