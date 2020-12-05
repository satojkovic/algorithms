#!/usr/bin/env python
# -*- coding=utf-8 -*-

class HashEntry:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None

class HashSet:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.bucket = self.capacity * [None]
        self.size = 0

    def _hash(self, key):
        return (hash(key) & 0x7fffffff) % self.capacity

    def _bucket_seek(self, h, key):
        head = self.bucket[h]
        pos = 0
        while head:
            if head.key == key:
                return pos
            head = head.next
            pos += 1
        return -1

    def add(self, key):
        h = self._hash(key)
        if self._bucket_seek(h, key) < 0:
            head = self.bucket[h]
            node = HashEntry(key)
            node.next = head
            self.bucket[h] = node
            self.size += 1

    def contains(self, key):
        h = self._hash(key)
        return self._bucket_seek(h, key) >= 0

    def remove(self, key):
        h = self._hash(key)
        pos = self._bucket_seek(h, key)
        if pos < 0:
            return False
        elif pos == 0:
            head = self.bucket[h]
            self.bucket[h] = head.next
        else:
            head = self.bucket[h]
            while pos > 1:
                head = head.next
                pos -= 1
            head.next = head.next.next
        self.size -= 1
        return True
