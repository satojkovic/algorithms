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


class QueueByList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.q = [0 for _ in range(self.capacity)]

    def is_empty(self):
        # Queue is empty when head and tail are at same position.
        return self.head == self.tail

    def is_full(self):
        return (self.tail + 1 == self.head) or \
            (self.head == 0 and (self.tail == self.capacity - 1))

    def enque(self, data):
        if self.is_full():
            return None
        self.q[self.tail] = data
        self.tail = (self.tail + 1) % self.capacity

    def deque(self):
        if self.is_empty():
            return None
        ret = self.q[self.head]
        self.head = (self.head + 1) % self.capacity
        return ret


def test_queue():
    ql = QueueByList(6)
    ql.enque(4)
    ql.enque(1)
    ql.enque(3)
    ql.deque()
    ql.enque(8)
    ql.deque()
    assert ql.head == 2
    assert ql.tail == 4

    ql.deque()
    ql.deque()
    assert ql.is_empty() is True
    assert ql.deque() is None

    [ql.enque(i*10) for i in range(6)]
    assert ql.is_full() is True
    ql.deque()
    ql.enque(100)
    assert ql.is_full() is True
    assert ql.enque(1000) is None
