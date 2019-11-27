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

    def add_at_head(self, val):
        # Add a node to the head of the linked list, O(1)
        node = DoublyListElement(val)
        node.next_elem = self.head
        if self.head:
            self.head.prev_elem = node
        self.head = node

    def add_at_tail(self, val):
        # Add a node to the tail of the linked list, O(n)
        if self.is_empty():
            self.add_at_head(val)
        else:
            curr = self.head
            while curr.next_elem:
                curr = curr.next_elem
            node = DoublyListElement(val)
            curr.next_elem = node
            node.prev_elem = curr

    # Need to search the node x before deleting
    def delete(self, x):
        if x is None:
            return False

        if x.prev_elem:
            x.prev_elem.next_elem = x.next_elem
        else:
            self.head = x.next_elem
        if x.next_elem:
            x.next_elem.prev_elem = x.prev_elem

        return True