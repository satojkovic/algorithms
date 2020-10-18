#!/usr/bin/env python
# -*- coding=utf-8 -*-

class ListElement:
    """List Element of Singly Linked List
    """

    def __init__(self, data):
        self.data = data
        self.next_elem = None

def remove_nth_from_end(head, n):
    if head is None:
        return None
    slow = head
    fast = head
    # forward the fast pointer by n+1 times
    while n >= 0 and fast:
        fast = fast.next_elem
        n -= 1
    # forward the fast pointer until the tail and move the slow pointer at the same time.
    while fast:
        fast = fast.next_elem
        slow = slow.next_elem
    # when the fast pointer reach to the tail, remove target is the next node of slow pointer.
    # however when the length of this linked list is n, remove target is head node.
    if n == 0:
        head = slow.next_elem
    else:
        slow.next_elem = slow.next_elem.next_elem
    return head

def remove_nth_from_end2(head, n):
    def helper(head, n, i):
        if head is None:
            return head, i
        node, l = helper(head.next_elem, n, i + 1)
        if (l - n) != i:
            head.next_elem = node
            return head, l
        else:
            return node, l
    head, l = helper(head, n, 0)
    return head

def reverse_list(head):
    if head is None:
        return head
    new_head = None
    while head:
        next_head = head.next_elem
        head.next_elem = new_head
        new_head = head
        head = next_head
    return new_head

def reverse_list_r(head):
    def reverse(head, prev_head):
        if head is None:
            return prev_head
        next_head = head.next_elem
        head.next_elem = prev_head
        return reverse(next_head, head)
    return reverse(head, None)

def remove_target_node(head, target):
    if head is None:
        return head
    head.next_elem = remove_target_node(head.next_elem, target)
    return head if head.data != target else head.next_elem

def odd_even_order(head):
    if head is None:
        return head
    odd, even = head, head.next_elem
    odd_h, even_h = odd, even
    while odd.next_elem and odd.next_elem.next_elem:
        odd.next_elem = even.next_elem
        even.next_elem = odd.next_elem.next_elem
        odd = odd.next_elem
        even = even.next_elem
    odd.next_elem = even_h
    return odd_h

def is_palindrome(head):
    if head is None:
        return True
    list_len = list_length(head)
    ret, _ = check_palindrome(head, list_len, 0)
    return ret

def list_length(head):
    if head is None:
        return 0
    return list_length(head.next_elem) + 1

def check_palindrome(head, list_len, pos):
    if pos == (list_len // 2):
        return (True, head.next_elem) if (list_len % 2) != 0 else (True, head)
    ret, node = check_palindrome(head.next_elem, list_len, pos + 1)
    if ret and head.data == node.data:
        return (True, node.next_elem)
    else:
        return (False, node.next_elem)

def is_palindrome2(head):
    # find the middle node
    fast = slow = head
    while fast and fast.next_elem:
        fast = fast.next_elem.next_elem
        slow = slow.next_elem
    # reverse the latter half
    prev_node = None
    while slow:
        next_node = slow.next_elem
        slow.next = prev_node
        prev_node = slow
        slow = next_node
    # compare former and latter half
    while prev_node:
        if prev_node.data != head.data:
            return False
        prev_node = prev_node.next_elem
        head = head.next_elem
    return True

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
        node.next_elem = self.head
        self.head = node
        self.size += 1

    def add_tail(self, elem):
        # Add a node to the tail of the linked list, O(n)
        if self.is_empty():
            self.head = ListElement(elem)
        else:
            node = self.head
            while node.next_elem:
                node = node.next_elem
            node.next_elem = ListElement(elem)
        self.size += 1

    def peek_head(self):
        # Return the value of the head node if it exists, O(1)
        return self.head.data if not self.is_empty() else None

    def peek_tail(self):
        # Check the value of the last node if it exits, O(n)
        if self.is_empty():
            return None
        node = self.head
        while node.next_elem:
            node = node.next_elem
        return node.data

    def remove_head(self):
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
            return self.remove_head()

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
            return self.remove_head()

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

    def _reverse_list(self, head):
        if head.next_elem is None:
            return head
        rhead = self._reverse_list(head.next_elem)
        head.next_elem.next_elem = head
        head.next_elem = None
        return rhead

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
