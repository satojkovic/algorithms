#!/usr/bin/env python
# -*- coding=utf-8 -*-

class HashEntry:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None

class HashSet:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bucket = self.capacity * [None]
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def add(self, key):
        h = self._hash(key)
        if self.bucket[h] is None:
            self.bucket[h] = HashEntry(key)
        else:
            head = self.bucket[h]
            while head.next:
                head = head.next
            head.next = HashEntry(key)
        self.size += 1

    def contains(self, key):
        h = self._hash(key)
        if self.bucket[h] is None:
            return False
        else:
            head = self.bucket[h]
            while head:
                if head.key == key:
                    return True
                head = head.next
            return False