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
        return self.head is None

    def enque(self, data):
        elem = QueueElem(data)
        if self.tail is not None:
            self.tail.next = elem
        self.tail = elem
        if self.head is None:
            self.head = elem

    def deque(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def print_queue(self):
        if self.head is None:
            print('Queue is empty.')
            return

        elem = self.head
        while elem:
            print(elem.data, end='->')
            elem = elem.next
        print('None')

class QueueByList:
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.q = [0 for _ in range(self.capacity)]

    def is_empty(self):
        return (self.size == 0)

    def enque(self, val):
        self.q[self.tail] = val
        self.tail += 1
        if self.tail == self.capacity:
            self.tail = 0
        if self.size < self.capacity:
            self.size += 1

    def deque(self):
        if self.is_empty():
            return -1
        ret = self.q[self.head]
        self.head += 1
        if self.head == self.capacity:
            self.head = 0
        if self.size > 0:
            self.size -= 1
        return ret

    def print_queue(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            for i in range(self.size):
                print(self.q[(self.head + i) % self.capacity])

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

    ql = QueueByList()
    print('---')
    ql.enque(1)
    ql.enque(2)
    ql.enque(3)
    ql.print_queue()
    print('---')
    ql.enque(4)
    ql.print_queue()
    print('---')

    print(ql.deque())
    print(ql.deque())
    print(ql.deque())
    print(ql.deque())
    print(ql.deque())