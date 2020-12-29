#!/usr/bin/env python
# -*- coding=utf-8 -*-

class DoublyListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        # check whether the size equal zero
        return self.size == 0

    def search(self, k):
        x = self.head
        while x and x.data != k:
            x = x.next
        return x

    def find(self, index):
        if index >= self.size or index < 0:
            return None
        curr = self.head
        while index:
            curr = curr.next
            index -= 1
        return curr

    def get(self, index):
        if index >= self.size or index < 0:
            return -1
        curr = self.head
        while index:
            curr = curr.next
            index -= 1
        return curr.data

    def add_at_head(self, data):
        # Add a node to the head of the linked list, O(1)
        node = DoublyListNode(data)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        self.size += 1

    def add_at_tail(self, data):
        # Add a node to the tail of the linked list, O(n)
        if self.is_empty():
            self.add_at_head(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            node = DoublyListNode(data)
            curr.next = node
            node.prev = curr
            self.size += 1

    def add_at_index(self, index, data):
        # Accept when index == self.size because that means add_at_tail()
        if index > self.size or index < 0:
            return None
        if index == 0:
            self.add_at_head(data)
        elif index == self.size:
            self.add_at_tail(data)
        else:
            curr = self.find(index)
            node = DoublyListNode(data)
            node.prev = curr.prev
            node.next = curr
            curr.prev.next = node
            curr.prev = node
            self.size += 1

    def delete_at_index(self, index):
        if index >= self.size or index < 0:
            return None
        curr = self.find(index)
        if curr.prev is None:
            self.head = curr.next
        else:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        curr.next = None
        curr.prev = None
        self.size -= 1

    # Need to search the node x before deleting
    def delete(self, x):
        if x is None:
            return False

        if x.prev:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next:
            x.next.prev = x.prev

        return True