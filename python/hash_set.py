#!/usr/bin/env python
# -*- coding=utf-8 -*-

class HashEntry:
    def __init__(self, key):
        self.key = key
        self.next = None

class HashSet:
    def __init__(self, size):
        self.size = size
        self.bucket = self.size * [None]

    def _map_bucket_idx(self, key):
        return hash(key) % self.size

    def _bucket_seek(self, key):
        idx = self._map_bucket_idx(key)
        head = self.bucket[idx]
        pos = 0
        while head:
            if head.key == key:
                return pos
            head = head.next
            pos += 1
        return -1

    def add(self, key):
        idx = self._map_bucket_idx(key)
        if not self.contains(key):
            node = HashEntry(key)
            node.next = self.bucket[idx]
            self.bucket[idx] = node

    def contains(self, key):
        return self._bucket_seek(key) >= 0

    def remove(self, key):
        idx = self._map_bucket_idx(key)
        head = self.bucket[idx]
        if head is None:
            return None
        if head.key == key:
            self.bucket[idx] = head.next
            return key
        while head.next and head.next.key != key:
            head = head.next
        if head.next:
            head.next = head.next.next
            return key
        return None