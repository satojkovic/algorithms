#!/usr/bin/env python
# -*- coding=utf-8 -*-

class QueueElem:
    def __init__(self, data):
        self.data = data
        self.next_elem = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return not self.head and not self.tail

    def enque(self, data):
        elem = QueueElem(data)
        if self.tail is None:
            self.tail = elem
        else:
            self.tail.next_elem = elem
            self.tail = elem
        if self.head is None:
            self.head = elem

    def deque(self):
        if self.head is None and self.tail is None:
            return None
        ret = self.head.data
        self.head = self.head.next_elem
        if not self.head:
            self.tail = self.head
        return ret

    def print_queue(self):
        if self.is_empty():
            print('Queue is empty.')
            return

        elem = self.head
        while elem:
            print(elem.data, end='->')
            elem = elem.next_elem
        print('None')

if __name__ == "__main__":
    q = Queue()
    q.print_queue()
    print('enque(10)')
    q.enque(10)
    print('enque(1)')
    q.enque(1)
    print('enque(6)')
    q.enque(6)
    q.print_queue()

    print('deque():', q.deque())
    print('deque():', q.deque())
    print('deque():', q.deque())
    print('deque():', q.deque())
    q.print_queue()