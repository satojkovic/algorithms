#!/usr/bin/env python
# -*- coding=utf-8 -*-

class PQueue:
    def __init__(self, data=[]):
        self.heap = data
        self.size = len(self.heap)

        if self.size != 0 and self.size != 1:
            last_idx = self.size - 1
            last_pidx = (last_idx - 2) // 2 if last_idx % 2 == 0 else (last_idx - 1) // 2
            for p in range(last_pidx, -1, -1):
                self.heap = self.heapify(self.heap, p, last_idx)

    def heapify(self, data, p, last_idx):
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

        if left_idx <= last_idx and data[smallest] > data[left_idx]:
            smallest = left_idx
        if right_idx <= last_idx and data[smallest] > data[right_idx]:
            smallest = right_idx

        if smallest != p:
            data[smallest], data[p] = data[p], data[smallest]
            data = self.heapify(data, smallest, last_idx)
        
        return data

    def add(self, data):
        self.heap.append(data)
        self.size += 1

        if self.size != 1:
            # Keep heap invariant
            last_idx = self.size - 1
            last_pidx = (last_idx - 2) // 2 if last_idx % 2 == 0 else (last_idx - 1) // 2
            while last_pidx >= 0:
                self.heap = self.heapify(self.heap, last_pidx, last_idx)
                last_pidx = (last_pidx - 2) // 2 if last_pidx % 2 == 0 else (last_pidx - 1) // 2

if __name__ == "__main__":
    pq = PQueue([5, 6, 8, 7, 12, 14, 19, 13, 12, 11])
    pq.add(1)
    print(pq.heap)
