#!/usr/bin/env python
# -*- coding=utf-8 -*-

def heapify(data, p, n):
    left_idx = 2 * p + 1
    right_idx = 2 * p + 2
    largest = p
    if left_idx <= n and data[largest] < data[left_idx]:
        largest = left_idx
    if right_idx <= n and data[largest] < data[right_idx]:
        largest = right_idx
    if largest != p:
        data[largest], data[p] = data[p], data[largest]
        data = heapify(data, largest, n)
    return data

def heap_sort(data):
    """heap sort

    Fist, we build the heap from the given input list.
    We create a max heap to sort input list in ascending order. 
    Once the heap is created we swap the root node with the last node and 
    exclude the last node from next heapify.
    
    Args:
        data (list): an input list
    
    Returns:
        list: a list which is sorted in ascending order
    """
    if not data:
        return None
    if len(data) < 2:
        return data

    last_idx = len(data) - 1
    last_pidx = (len(data) - 1) // 2
    for p in range(last_pidx, -1, -1):
        data = heapify(data, p, last_idx)

    for i in range(last_idx, 0, -1):
        data[i], data[0] = data[0], data[i]
        data = heapify(data, 0, i - 1)

    return data


if __name__ == "__main__":
    data = [6, 5, 1, 8, 2, 4]
    print('heap sort {} => '.format(data), end='')
    print('{}'.format(heap_sort(data)))