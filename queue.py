#!/usr/bin/env python
# -*- coding=utf-8 -*-

class QueueElem:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return not self.head and not self.tail

    def enque(self, data):
        elem = QueueElem(data)
        if self.is_empty():
            self.head = elem
            self.tail = self.head
        else:
            self.tail.next = elem
            self.tail = self.tail.next

    def deque(self):
        if self.is_empty():
            return None
        ret = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return ret

    def print_queue(self):
        if self.is_empty():
            print('Queue is empty.')
            return

        elem = self.head
        while elem:
            print(elem.data, end='->')
            elem = elem.next
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