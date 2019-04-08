#!/usr/bin/env python
# -*- coding=utf-8 -*-

class Array:
    def __init__(self, capacity=16):
        if capacity < 0:
            self.capacity = 16
        else:
            self.capacity = capacity
        self.arr = [0] * capacity
        self.length = 0

    def size(self):
        return self.length

    def is_empty(self):
        return self.size() == 0

    def clear(self):
        for i in range(self.capacity):
            self.arr[i] = 0
        self.length = 0
