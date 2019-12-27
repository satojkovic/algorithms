#!/usr/bin/env python
# -*- coding=utf-8 -*-

class HashSet:
    def __init__(self, size):
        self.size = size
        self.data = self.size * [0]

    def add(self, key):
        h = hash(key) % self.size
        self.data[h] = key