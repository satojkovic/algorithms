#!/usr/bin/env python
# -*- coding=utf-8 -*-

class MaxHeap:
    def __init__(self):
        self.data = []

    def heapify(self, data, p, size):
        """Build a max heap

        In a max heap, the parent node is always greater than or equal to its child nodes.
        If p denotes the index of a parent node, then 2*p + 1 denotes the left child node and
        2*p + 2 denotes the right child node.

        A node with largest value among parent and child nodes will be a new parent node,
        and building a max heap is repeated to a subtree of a child node swapped by previous parent node.

        Args:
            data (list): an input list
            p (integer): a parent node index

        Returns:
            list: returns a max heap represented as one dimensional array
        """
        left_idx = 2 * p + 1
        right_idx = 2 * p + 2
        largest = p

        if left_idx < size and data[largest] < data[left_idx]:
            largest = left_idx
        if right_idx < size and data[largest] < data[right_idx]:
            largest = right_idx

        if largest != p:
            data[largest], data[p] = data[p], data[largest]
            data = self.heapify(data, largest, size)

        return data

    def build(self, data):
        tail = len(data) - 1
        parent = (tail - 1) // 2
        for p in range(parent, -1, -1):
            data = self.heapify(data, p, size=len(data))
        self.data = data

    def push(self, val):
        self.data.append(val)
        curr = len(self.data) - 1
        while curr > 0:
            parent = (curr - 1) // 2
            if self.data[parent] >= self.data[curr]:
                break
            self.data[parent], self.data[curr] = self.data[curr], self.data[parent]
            curr = parent

    def pop(self):
        if len(self.data) == 0:
            return None
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        ret = self.data.pop()
        curr = 0
        data_size = len(self.data)
        while curr < data_size:
            left_idx = 2 * curr + 1
            right_idx = 2 * curr + 2
            largest = curr
            if left_idx < data_size and self.data[largest] < self.data[left_idx]:
                largest = left_idx
            if right_idx < data_size and self.data[largest] < self.data[right_idx]:
                largest = right_idx
            if largest == curr:
                break
            self.data[largest], self.data[curr] = self.data[curr], self.data[largest]
            curr = largest
        return ret


class MinHeap:
    def __init__(self):
        self.heap = []

    def _shift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[parent] > self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break

    def _shift_down(self, idx):
        data_size = len(self.heap)
        while idx < data_size:
            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2
            smallest = idx
            if left_idx < data_size and self.heap[smallest] > self.heap[left_idx]:
                smallest = left_idx
            if right_idx < data_size and self.heap[smallest] > self.heap[right_idx]:
                smallest = right_idx
            if smallest == idx:
                break
            self.heap[smallest], self.heap[idx] = self.heap[idx], self.heap[smallest]
            idx = smallest

    def push(self, val):
        self.heap.append(val)
        self._shift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        ret = self.heap.pop()
        self._shift_down(0)
        return ret

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def __len__(self):
        return len(self.heap)


# data from Algorithm Introduction 3rd edition
def test_max_heap():
    max_heap = MaxHeap()
    max_heap.build([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    assert max_heap.data == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]


def test_min_heap():
    min_heap = MinHeap()
    values = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    for val in values:
        min_heap.push(val)
    assert min_heap.heap == [1, 2, 3, 4, 7, 9, 10, 14, 8, 16]
