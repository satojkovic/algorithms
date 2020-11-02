#!/usr/bin/env python
# -*- coding=utf-8 -*-

class ListElement:
    """List Element of Singly Linked List
    """

    def __init__(self, data):
        self.data = data
        self.next = None

def remove_nth_from_end(head, n):
    if head is None:
        return None
    slow = head
    fast = head
    # forward the fast pointer by n+1 times
    while n >= 0 and fast:
        fast = fast.next
        n -= 1
    # forward the fast pointer until the tail and move the slow pointer at the same time.
    while fast:
        fast = fast.next
        slow = slow.next
    # when the fast pointer reach to the tail, remove target is the next node of slow pointer.
    # however when the length of this linked list is n, remove target is head node.
    if n == 0:
        head = slow.next
    else:
        slow.next = slow.next.next
    return head

def remove_nth_from_end2(head, n):
    def helper(head, n, i):
        if head is None:
            return head, i
        node, l = helper(head.next, n, i + 1)
        if (l - n) != i:
            head.next = node
            return head, l
        else:
            return node, l
    head, l = helper(head, n, 0)
    return head

def reverse_list(head):
    new_head = None
    while head:
        next_head = head.next
        head.next = new_head
        new_head = head
        head = next_head
    return new_head

def reverse_list_r(head):
    def reverse(head, prev_head):
        if head is None:
            return prev_head
        next_head = head.next
        head.next = prev_head
        return reverse(next_head, head)
    return reverse(head, None)

def remove_target_node(head, target):
    if head is None:
        return head
    head.next = remove_target_node(head.next, target)
    return head if head.data != target else head.next

def odd_even_order(head):
    if head is None:
        return head
    odd, even = head, head.next
    odd_h, even_h = odd, even
    while odd.next and odd.next.next:
        odd.next = even.next
        even.next = odd.next.next
        odd = odd.next
        even = even.next
    odd.next = even_h
    return odd_h

def list_length(head):
    if head is None:
        return 0
    return list_length(head.next) + 1

class LinkedList:
    """Linked List
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        # check whether the size equal zero
        return self.size == 0

    def clear(self):
        # clear the linked list
        self.head = None
        self.size = 0

    def add(self, elem):
        # Add always append the new node at the tail
        self.add_tail(elem)

    def add_head(self, elem):
        # Add a node to the head of the linked list, O(1)
        node = ListElement(elem)
        node.next = self.head
        self.head = node
        self.size += 1

    def add_tail(self, elem):
        # Add a node to the tail of the linked list, O(n)
        if self.is_empty():
            self.head = ListElement(elem)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = ListElement(elem)
        self.size += 1

    def peek_head(self):
        # Return the value of the head node if it exists, O(1)
        return self.head.data if not self.is_empty() else None

    def peek_tail(self):
        # Check the value of the last node if it exits, O(n)
        if self.is_empty():
            return None
        node = self.head
        while node.next:
            node = node.next
        return node.data

    def remove_head(self):
        if self.is_empty():
            return None
        # Extract the data at the head and move the head pointer forwards one node
        data = self.head.data
        self.head = self.head.next
        self.size -= 1

        # Return the data that was at the head we just removed
        return data

    def remove_last(self):
        if self.is_empty():
            return None

        trav1 = self.head
        trav2 = self.head.next
        if not trav2:
            return self.remove_head()

        while trav2.next:
            trav1 = trav1.next
            trav2 = trav2.next
        data = trav2.data
        trav1.next = trav2.next
        self.size -= 1

        return data

    # Remove a particular node in the linked list, O(n)
    def remove(self, node):
        if self.is_empty():
            return False
        # if the node to remove is somewhere either at the head or the tail
        # handle those independently
        if node.data == self.head.data:
            return self.remove_head()

        # search for a target node
        trav1 = self.head
        trav2 = self.head.next
        while trav2:
            if trav2.data == node.data:
                trav1.next = trav2.next
                self.size -= 1
                return True
            trav1 = trav1.next
            trav2 = trav2.next
        return False

    def search(self, node):
        if self.is_empty():
            return None
        p = self.head
        while p:
            if p.data == node.data:
                return True
            p = p.next
        return False

    def reverse_list(self):
        def reverse(head):
            new_head = None
            while head:
                next_head = head.next
                head.next = new_head
                new_head = head
                head = next_head
            return new_head
        return reverse(self.head)

    def find_middle(self):
        if self.is_empty():
            return None

        fast = self.head
        slow = self.head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data

    def detect_loop(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
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
                curr = curr.next
            else:
                return curr
        return None

    def remove_dups(self):
        if self.is_empty():
            return None

        uniqs = set()
        dups = set()
        head = self._remove_dups(self.head, uniqs, dups)
        self.head = head.next if head.data in dups else head
        print('uniqs:', uniqs)
        print('dups:', dups)
        return True

    def _remove_dups(self, head, uniqs, dups):
        if not head:
            return head

        if head.data in uniqs:
            dups.add(head.data)
        uniqs.add(head.data)
        node = self._remove_dups(head.next, uniqs, dups)
        if node and node.data in dups:
            head.next = node.next
        else:
            head.next = node
        return head

    def print_list(self):
        if self.is_empty():
            print('List is empty.')
            return
        temp = self.head
        print('List:', end=' ')

        while temp:
            print(temp.data, end='->')
            temp = temp.next
        print('None')
