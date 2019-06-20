#!/usr/bin/env python
# -*- coding=utf-8 -*-

class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=3, load_factor=0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = self.capacity * [None]

    def is_empty(self):
        return self.size == 0

    def _get_index(self, key):
        return (hash(key) & 0x7fffffff) % self.capacity

    def bucket_seek(self, bucket_index, key):
        if key is None:
            return None

        bucket = self.table[bucket_index]
        if not bucket:
            return None
        head = bucket
        while head:
            if head.key == key:
                return head
            head = head.next
        return None
