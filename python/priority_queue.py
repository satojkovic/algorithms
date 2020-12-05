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

    def is_empty(self):
        return self.size == 0

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

    def poll(self):
        if self.is_empty():
            return None

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        ret = self.heap.pop()
        self.size -= 1

        last_idx = self.size - 1
        last_pidx = (last_idx - 2) // 2 if last_idx % 2 == 0 else (last_idx - 1) // 2
        for p in range(last_pidx, -1, -1):
            self.heap = self.heapify(self.heap, p, last_idx)

        return ret

    def search(self, data):
        return self.heap.index(data) if data in self.heap else None

    def remove(self, data):
        if self.is_empty():
            return None

        target_idx = self.search(data)
        if not target_idx:
            return None

        self.heap[target_idx], self.heap[-1] = self.heap[-1], self.heap[target_idx]
        ret = self.heap.pop()
        self.size -= 1

        # keep heap invariant
        last_idx = self.size - 1
        if 2 * target_idx + 1 > last_idx:
            # bubble up
            target_pidx = (target_idx - 2) // 2 if target_idx % 2 == 0 else (target_idx - 1) // 2
            while target_pidx >= 0:
                self.heap = self.heapify(self.heap, target_pidx, target_idx)
                target_pidx = (target_pidx - 2) // 2 if target_pidx % 2 == 0 else (target_pidx - 1) // 2
        else:
            # bubble down
            target_pidx = target_idx
            self.heap = self.heapify(self.heap, target_pidx, last_idx)

        return ret

    def print_pqueue(self):
        if self.is_empty():
            print('PQueue is empty.')
            return

        print('Current PQueue: size =', self.size)
        depth = 0
        next_line = 2 ** depth
        for i in range(self.size):
            print(self.heap[i], end=' ')
            if (i + 1) == next_line:
                print()
                depth += 1
                next_line += 2 ** depth
        print()

if __name__ == "__main__":
    pq = PQueue([5, 6, 8, 7, 15, 14, 19, 13, 12, 11])
    print(pq.heap)
    pq.add(1)
    print('add()')
    pq.print_pqueue()

    print('poll()')
    ret = pq.poll()
    print('return value:', ret)
    pq.print_pqueue()

    target = 6
    print('remove({})'.format(target))
    ret = pq.remove(target)
    print('return value:', ret)
    pq.print_pqueue()