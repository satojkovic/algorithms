#!/usr/bin/env python
# -*- coding=utf-8 -*-

class MaxHeap:
    def __init__(self):
        self.size = 0
        self.data = []

    def heapify(self, data, p):
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

        if left_idx < len(data) and data[largest] < data[left_idx]:
            largest = left_idx
        if right_idx < len(data) and data[largest] < data[right_idx]:
            largest = right_idx

        if largest != p:
            data[largest], data[p] = data[p], data[largest]
            data = self.heapify(data, largest)

        return data

    def build(self, data):
        last_pidx = (len(data) - 1) // 2
        for p in range(last_pidx, -1, -1):
            data = self.heapify(data, p)
        self.data = data
        self.size = len(self.data)

    def push(self, val):
        self.data.append(val)
        self.size += 1
        curr = len(self.data) - 1
        while curr > 0:
            parent = (curr - 1) // 2
            if self.data[parent] >= self.data[curr]:
                break
            self.data[parent], self.data[curr] = self.data[curr], self.data[parent]
            curr = parent

    def pop(self):
        if self.size == 0:
            return None
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        ret = self.data.pop()
        self.size -= 1
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
        self.size = 0
        self.data = []

    def heapify(self, data, p):
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
    
    def build(self, data):
        last_pidx = (len(data) - 1) // 2
        for p in range(last_pidx, -1, -1):
            data = self.heapify(data, p)
        self.data = data
        self.size = len(self.data)

    def push(self, val):
        self.data.append(val)
        self.size += 1
        curr = len(self.data) - 1
        while curr > 0:
            parent = (curr - 1) // 2
            if self.data[parent] <= self.data[curr]:
                break
            self.data[parent], self.data[curr] = self.data[curr], self.data[parent]
            curr = parent

    def pop(self):
        if self.size == 0:
            return None
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        ret = self.data.pop()
        self.size -= 1
        curr = 0
        data_size = len(self.data)
        while curr < data_size:
            left_idx = 2 * curr + 1
            right_idx = 2 * curr + 2
            smallest = curr
            if left_idx < data_size and self.data[smallest] > self.data[left_idx]:
                smallest = left_idx
            if right_idx < data_size and self.data[smallest] > self.data[right_idx]:
                smallest = right_idx
            if smallest == curr:
                break
            self.data[smallest], self.data[curr] = self.data[curr], self.data[smallest]
            curr = smallest
        return ret

if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.build([6, 5, 1, 8, 2, 4])
    print(max_heap.data)
    max_heap.push(10)
    print(max_heap.data)
    for i in range(len(max_heap.data)):
        print('pop()=>{}'.format(max_heap.pop()))
    print('pop()=>{}'.format(max_heap.pop()))

    min_heap = MinHeap()
    min_heap.build([6, 5, 1, 8, 2, 4])
    print(min_heap.data)
    min_heap.push(0)
    print(min_heap.data)
    for i in range(len(min_heap.data)):
        print('pop()=>{}'.format(min_heap.pop()))
    print('pop()=>{}'.format(min_heap.pop()))