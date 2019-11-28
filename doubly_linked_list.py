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
        self.size = 0

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

    def find(self, index):
        if index >= self.size or index < 0:
            return None
        curr = self.head
        while index:
            curr = curr.next_elem
            index -= 1
        return curr

    def get(self, index):
        if index >= self.size or index < 0:
            return -1
        curr = self.head
        while index:
            curr = curr.next_elem
            index -= 1
        return curr.data

    def add_at_head(self, val):
        # Add a node to the head of the linked list, O(1)
        node = DoublyListElement(val)
        node.next_elem = self.head
        if self.head:
            self.head.prev_elem = node
        self.head = node
        self.size += 1

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
            self.size += 1

    def add_at_index(self, index, val):
        # Accept when index == self.size because that means add_at_tail()
        if index > self.size or index < 0:
            return None
        if index == 0:
            self.add_at_head(val)
        elif index == self.size:
            self.add_at_tail(val)
        else:
            curr = self.find(index)
            node = DoublyListElement(val)
            node.prev_elem = curr.prev_elem
            node.next_elem = curr
            curr.prev_elem.next_elem = node
            curr.prev_elem = node
            self.size += 1

    def delete_at_index(self, index):
        if index >= self.size or index < 0:
            return None
        curr = self.find(index)
        if curr.prev_elem is None:
            self.head = curr.next_elem
        else:
            curr.prev_elem.next_elem = curr.next_elem
        if curr.next_elem:
            curr.next_elem.prev_elem = curr.prev_elem
        curr.next_elem = None
        curr.prev_elem = None
        self.size -= 1

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