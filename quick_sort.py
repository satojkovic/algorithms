#!/usr/bin/env python
# -*- coding=utf-8 -*-

def quick_sort(data):
    """quick sort

    quick sort is executed in the following steps.

    1. select a pivot, make left and right list with a value greater and smaller than pivot respectively.
    2. quick sort smaller list recursively.
    3. quick sort larger list recursively.
    4. concatenate sorted smaller and equal and right.

    Args:
        data (list): an input list

    Returns:
        list: a new sorted list
    """
    if len(data) <= 1:
        return data
    smaller, equal, larger = [], [], []
    pivot = data[len(data)// 2]
    for d in data:
        if d < pivot: smaller.append(d)
        elif d == pivot: equal.append(d)
        else: larger.append(d)
    return quick_sort(smaller) + equal + quick_sort(larger)


def quick_sort_in_place(data):
    """quick sort in place partition

    Args:
        data (list): an input list

    Returns:
        list: a sorted list
    """
    return _quick_sort(data, 0, len(data) - 1)


def _quick_sort(data, l, r):
    if l >= r:
        return
    mid = partition(data, l, r)
    _quick_sort(data, l, mid - 1)
    _quick_sort(data, mid + 1, r)
    return data


def partition(data, l, r):
    i, j = l, l
    pivot = data[r]
    for current in range(l, r):
        if data[current] > pivot:
            j += 1
        elif data[current] <= pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
            j += 1
    data[i], data[r] = data[r], data[i]
    return i


if __name__ == "__main__":
    data = [30, 2, 10, 100, 24, 7, 79]
    print('org:', data)
    print('sorted:', quick_sort(data))

    data = [30, 2, 10, 100, 24, 7, 79]
    print('sorted(in place):', quick_sort_in_place(data))