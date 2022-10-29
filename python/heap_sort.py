#!/usr/bin/env python
# -*- coding=utf-8 -*-


# To heapify subtree rooted at index p.
def heapify(data, p, size):
    left_idx = 2 * p + 1
    right_idx = 2 * p + 2
    largest = p
    if left_idx < size and data[largest] < data[left_idx]:
        largest = left_idx
    if right_idx < size and data[largest] < data[right_idx]:
        largest = right_idx
    if largest != p:
        data[largest], data[p] = data[p], data[largest]
        data = heapify(data, largest, size)
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

    parent = (len(data) - 1) // 2
    for p in range(parent, -1, -1):
        data = heapify(data, p, size=len(data))

    tail = len(data) - 1
    size = len(data)
    for i in range(tail, 0, -1):
        data[i], data[0] = data[0], data[i]
        size -= 1
        data = heapify(data, 0, size=size)

    return data


def test_heap_sort():
    assert heap_sort([6, 5, 1, 8, 2, 4]) == [1, 2, 4, 5, 6, 8]
    assert heap_sort([10, 1, 3, 7, 2]) == [1, 2, 3, 7, 10]
    assert heap_sort([10, 3]) == [3, 10]
    assert heap_sort([1]) == [1]
    assert heap_sort([]) == None
    assert heap_sort([1, 1, 1]) == [1, 1, 1]
