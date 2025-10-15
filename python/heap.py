#!/usr/bin/env python
# -*- coding=utf-8 -*-

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _shift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[parent] < self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break

    def _shift_down(self, idx):
        data_size = len(self.heap)
        while idx < data_size:
            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2
            largest = idx
            if left_idx < data_size and self.heap[largest] < self.heap[left_idx]:
                largest = left_idx
            if right_idx < data_size and self.heap[largest] < self.heap[right_idx]:
                largest = right_idx
            if largest == idx:
                break
            self.heap[largest], self.heap[idx] = self.heap[idx], self.heap[largest]
            idx = largest

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
    values = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    for val in values:
        max_heap.push(val)

    # Internal representation is irrelevant
    # If the results of the pop operation are in descending order, it is a valid max heap.
    sorted_values = sorted(values, reverse=True)
    popped_values = []
    while len(max_heap) > 0:
        popped_values.append(max_heap.pop())
    assert popped_values == sorted_values


def test_min_heap():
    min_heap = MinHeap()
    values = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    for val in values:
        min_heap.push(val)

    # Internal representation is irrelevant
    # If the results of the pop operation are in ascending order, it is a valid min
    sorted_values = sorted(values)
    popped_values = []
    while len(min_heap) > 0:
        popped_values.append(min_heap.pop())
    assert popped_values == sorted_values
