#!/usr/bin/env python
# -*- coding=utf-8 -*-

class ListElement:
    """List Element of Singly Linked List
    """

    def __init__(self, data):
        self.data = data
        self.next_elem = None


class LinkedList:
    """Linked List
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        # check whether head is None
        if not self.head:
            return True
        else:
            return False

    def clear(self):
        # clear the linked list, O(n)
        trav = self.head
        while not trav:
            next_elem = trav.next_elem
            trav.next_elem = None
            trav.data = None
            trav = next_elem

    def add(self, elem):
        self.add_last(elem)

    def add_first(self, elem):
        node = ListElement(elem)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next_elem = self.head
            self.head = node
        self.size += 1

    def add_last(self, elem):
        # Add a node to the tail of the linked list, O(1)
        if self.is_empty():
            node = ListElement(elem)
            self.head = node
            self.tail = node
        else:
            self.tail.next_elem = ListElement(elem)
            self.tail = self.tail.next_elem
        self.size += 1

    def print_list(self):
        if self.is_empty():
            print('List is empty.')
            return
        temp = self.head
        print('List:', end=' ')

        while temp:
            print(temp.data, end='->')
            temp = temp.next_elem
        print('None')

if __name__ == "__main__":
    l = LinkedList()
    [l.add(i) for i in range(10)]
    l.print_list()
    l.clear()
    [l.add_first(i) for i in range(10)]
    l.print_list()