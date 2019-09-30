#!/usr/bin/env python
# -*- coding=utf-8 -*-

class DoublyListElement:
    def __init__(self, data):
        self.data = data
        self.prev_elem = None
        self.next_elem = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def search(self, k):
        x = self.head
        while x and x.data != k:
            x = x.next_elem
        return x

    # O(1)
    def insert(self, x):
        x.next_elem = self.head
        if self.head:
            self.head.prev_elem = x
        self.head = x

    # Need to search the node x before deleting
    def delete(self, x):
        if x.prev_elem:
            x.prev_elem.next_elem = x.next_elem
        else:
            self.head = x.next_elem
        if x.next_elem:
            x.next_elem.prev_elem = x.prev_elem