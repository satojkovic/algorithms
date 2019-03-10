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

    def is_empty(self):
        # check whether head is None
        if not self.head:
            return True
        else:
            return False