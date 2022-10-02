#!/usr/bin/env python
# -*- coding=utf-8 -*-

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def build(self, data):
        curr = len(data) - 1
        parent = (curr - 1) // 2
        for p in range(parent, -1, -1):
            data = self.heapify(data, p)
        self.heap = data

    def is_empty(self):
        return len(self.heap) == 0

    def heapify(self, data, p):
        """Build a min heap

        In a min heap, the parent node is always less than or equal to its child nodes.
        If p denotes the index of a parent node, then 2*p + 1 denotes the left child node and
        2*p + 2 denotes the right child node.

        A node with smallest value among parent and child nodes will be a new parent node,
        and building a min heap is repeated to a subtree of a child node swapped by previous parent node.

        Args:
            data (list): an input list
            p (integer): a parent node index

        Returns:
            list: returns a min heap represented as one dimensional array
        """
        left_idx = 2 * p + 1
        right_idx = 2 * p + 2
        smallest = p
        if left_idx < len(data) and data[left_idx] < data[smallest]:
            smallest = left_idx
        if right_idx < len(data) and data[right_idx] < data[smallest]:
            smallest = right_idx
        if smallest != p:
            data[smallest], data[p] = data[p], data[smallest]
            data = self.heapify(data, smallest)
        return data

    def heappush(self, data):
        self.heap.append(data)
        if len(self.heap) != 1:
            # Keep heap invariant
            curr = len(self.heap) - 1
            parent = (curr - 1) // 2
            while parent >= 0:
                self.heap = self.heapify(self.heap, parent)
                parent = (parent - 1) // 2

    def heappop(self):
        if self.is_empty():
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        ret = self.heap.pop()

        curr = len(self.heap) - 1
        parent = (curr - 1) // 2
        for p in range(parent, -1, -1):
            self.heap = self.heapify(self.heap, p)
        return ret


def test_priority_queue():
    pq = PriorityQueue()
    assert pq.is_empty() == True
    pq.build([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    assert pq.heap == [1, 2, 3, 4, 7, 9, 10, 14, 8, 16]

    assert pq.heappop() == 1
    assert pq.heap == [2, 4, 3, 8, 7, 9, 10, 14, 16]
    assert pq.heappop() == 2
    assert pq.heap == [3, 4, 9, 8, 7, 16, 10, 14]

    pq.heappush(0)
    assert pq.heap == [0, 3, 9, 4, 7, 16, 10, 14, 8]

    assert pq.is_empty() == False
