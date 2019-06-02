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

    def add(self, elem):
        self.add_last(elem)

    def add_first(self, elem):
        node = ListElement(elem)
        if self.is_empty():
            self.head = node
        else:
            node.next_elem = self.head
            self.head = node
        self.size += 1

    def add_last(self, elem):
        # Add a node to the tail of the linked list, O(n)
        if self.is_empty():
            node = ListElement(elem)
            self.head = node
        else:
            node = self.head
            while node.next_elem:
                node = node.next_elem
            node.next_elem = ListElement(elem)
        self.size += 1

    def peek_first(self):
        # check the value of the first node if it exists, O(1)
        if self.is_empty():
            return None
        return self.head.data

    def peek_last(self):
        if self.is_empty():
            return None
        node = self.head
        while node.next_elem:
            node = node.next_elem
        return node.data

    def remove_first(self):
        if self.is_empty():
            return None
        # Extract the data at the head and move the head pointer forwards one node
        data = self.head.data
        self.head = self.head.next_elem
        self.size -= 1

        # Return the data that was at the head we just removed
        return data

    def remove_last(self):
        if self.is_empty():
            return None

        trav1 = self.head
        trav2 = self.head.next_elem
        if not trav2:
            return self.remove_first()

        while trav2.next_elem:
            trav1 = trav1.next_elem
            trav2 = trav2.next_elem
        data = trav2.data
        trav1.next_elem = trav2.next_elem
        self.size -= 1

        return data

    # Remove a particular node in the linked list, O(n)
    def remove(self, node):
        if self.is_empty():
            return False
        # if the node to remove is somewhere either at the head or the tail
        # handle those independently
        if node == self.head:
            return self.remove_first()

        # search for a target node
        trav1 = self.head
        trav2 = self.head.next_elem
        while trav2:
            if trav2 == node:
                trav1.next_elem = trav2.next_elem
                self.size -= 1
                return True
            trav1 = trav1.next_elem
            trav2 = trav2.next_elem
        return False

    def search(self, node):
        if self.is_empty():
            return None
        p = self.head
        while p:
            if p == node:
                return True
            p = p.next_elem
        return False

    def reverse_list(self):
        if self.is_empty():
            return None
        self.head = self._reverse_list(self.head)
        return self.head is None

    def _reverse_list(self, head):
        if head.next_elem is None:
            return head
        node = self._reverse_list(head.next_elem)
        head.next_elem.next_elem = head
        head.next_elem = None
        return node

    def find_middle(self):
        if self.is_empty():
            return 0

        if not self.head.next_elem:
            return self.head.data

        fast = self.head
        slow = self.head
        while fast.next_elem and fast.next_elem.next_elem:
            fast = fast.next_elem.next_elem
            slow = slow.next_elem
        return slow.data

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
    target = ListElement(7)
    print('search {}: {}'.format(target.data, l.search(target)))
    target = ListElement(8)
    print('search {}: {}'.format(target.data, l.search(target)))
    target = ListElement(1)
    print('search {}: {}'.format(target.data, l.search(target)))
    target = ListElement(10)
    print('search {}: {}'.format(target.data, l.search(target)))
    print('reversed:')
    l.reverse_list()
    l.print_list()

    print('find_middle:', l.find_middle())
