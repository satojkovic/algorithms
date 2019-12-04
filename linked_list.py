#!/usr/bin/env python
# -*- coding=utf-8 -*-

class ListElement:
    """List Element of Singly Linked List
    """

    def __init__(self, data):
        self.data = data
        self.next_elem = None


def find_intersection(ll1, ll2):
    if not ll1 or not ll2:
        return False

    elems1 = set()
    head1 = ll1
    while head1:
        elems1.add(head1)
        head1 = head1.next_elem

    head2 = ll2
    while head2:
        if head2 in elems1:
            return head2
        head2 = head2.next_elem

    return False


class LinkedList:
    """Linked List
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        # check whether head is None
        return True if not self.head else False

    def clear(self):
        # clear the linked list
        self.head = None

    def add(self, elem):
        # Add always append the new node at the tail
        self.add_last(elem)

    def add_first(self, elem):
        # Add a node to the head of the linked list, O(1)
        node = ListElement(elem)
        node.next_elem = self.head
        self.head = node
        self.size += 1

    def add_last(self, elem):
        # Add a node to the tail of the linked list, O(n)
        if self.is_empty():
            self.head = ListElement(elem)
        else:
            node = self.head
            while node.next_elem:
                node = node.next_elem
            node.next_elem = ListElement(elem)
        self.size += 1

    def peek_first(self):
        # Check the value of the first node if it exists, O(1)
        return self.head.data if not self.is_empty() else None

    def peek_last(self):
        # Check the value of the last node if it exits, O(n)
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
        if node.data == self.head.data:
            return self.remove_first()

        # search for a target node
        trav1 = self.head
        trav2 = self.head.next_elem
        while trav2:
            if trav2.data == node.data:
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
            if p.data == node.data:
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
            return None

        if not self.head.next_elem:
            return self.head.data

        fast = self.head
        slow = self.head
        while fast.next_elem and fast.next_elem.next_elem:
            fast = fast.next_elem.next_elem
            slow = slow.next_elem
        return slow.data

    def detect_loop(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next_elem:
            slow = slow.next_elem
            fast = fast.next_elem.next_elem
            # Compare with object id
            if slow == fast:
                return True
        return False

    def detect_loop_start(self):
        visited = set()
        curr = self.head
        while curr is not None:
            if not curr in visited:
                visited.add(curr)
                curr = curr.next_elem
            else:
                return curr
        return None

    def remove_dups(self):
        if self.is_empty():
            return None

        uniqs = set()
        dups = set()
        head = self._remove_dups(self.head, uniqs, dups)
        self.head = head.next_elem if head.data in dups else head
        print('uniqs:', uniqs)
        print('dups:', dups)
        return True

    def _remove_dups(self, head, uniqs, dups):
        if not head:
            return head

        if head.data in uniqs:
            dups.add(head.data)
        uniqs.add(head.data)
        node = self._remove_dups(head.next_elem, uniqs, dups)
        if node and node.data in dups:
            head.next_elem = node.next_elem
        else:
            head.next_elem = node
        return head

    def find_nth_from_end(self, n):
        if self.is_empty():
            return None

        trav1 = self.head
        length = 0
        while trav1:
            length += 1
            trav1 = trav1.next_elem

        steps = length - n
        if steps < 0 or steps >= length:
            return None
        trav2 = self.head
        for i in range(steps):
            trav2 = trav2.next_elem

        return trav2


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
