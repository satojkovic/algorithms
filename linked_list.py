#!/usr/bin/env python
# -*- coding=utf-8 -*-

class ListElement:
    """List Element of Singly Linked List
    """

    def __init__(self, data):
        self.data = data
        self.next_elem = None

    def __eq__(self, other):
        if isinstance(other, ListElement):
            return self.data == other.data
        return False

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
        # clear the linked list
        self.head = None
        self.tail = None

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

    def peek_first(self):
        # check the value of the first node if it exists, O(1)
        if self.is_empty():
            return None
        return self.head.data

    def peek_last(self):
        # check the value of the last node if it exists, O(1)
        if self.is_empty():
            return None
        return self.tail.data

    def remove_first(self):
        if self.is_empty():
            return None
        # Extract the data at the head and move the head pointer forwards one node
        data = self.head.data
        self.head = self.head.next_elem
        self.size -= 1

        # if the list is empty, set the tail to None
        if self.is_empty():
            self.tail = None

        # Return the data that was at the head we just removed
        return data

    def remove_last(self):
        if self.is_empty():
            return None

        p = self.head
        while p.next_elem != self.tail:
            p = p.next_elem
        data = self.tail.data
        p.next_elem = self.tail.next_elem
        self.tail = p
        return data

    # Remove a particular node in the linked list, O(n)
    def remove(self, node):
        if self.is_empty():
            return False
        # if the node to remove is somewhere either at the head or the tail
        # handle those independently
        if node == self.head:
            return self.remove_first()
        if node == self.tail:
            return self.remove_last()

        # search for a target node
        p = self.head
        while p.next_elem != None:
            if p.next_elem == node:
                p.next_elem = p.next_elem.next_elem
                return True
            p = p.next_elem
        return False

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
    print('peek first:', l.peek_first())
    print('peek last:', l.peek_last())
    l.clear()
    [l.add_first(i) for i in range(10)]
    l.print_list()
    print('peek first:', l.peek_first())
    print('peek last:', l.peek_last())
    print('remove first:', l.remove_first())
    l.print_list()
    print('remove last:', l.remove_last())
    l.print_list()
    target = ListElement(4)
    print('remove middle {}: {}'.format(target.data, l.remove(target)))
    l.print_list()
    target = ListElement(20)
    print('remove middle {}: {}'.format(target.data, l.remove(target)))
    l.print_list()