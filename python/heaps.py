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

if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.build([6, 5, 1, 8, 2, 4])
    print(max_heap.data)
