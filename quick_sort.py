#!/usr/bin/env python
# -*- coding=utf-8 -*-

def quick_sort(data):
    """quick sort

    quick sort is executed in the following steps.

    1. select a pivot, make left and right list with a value greater and smaller than pivot respectively.
    2. quick sort left list recursively.
    3. quick sort right list recursively.
    4. concatenate sorted left and right list.

    Args:
        data (list): an input list

    Returns:
        list: a new sorted list
    """
    if len(data) == 0 or len(data) == 1:
        return data
    left, right, pivot_val = split(data)
    # Sort each sublist recursively
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [pivot_val] + right

def split(data):
    left, right = [], []
    pivot_idx = len(data) // 2
    pivot_val = data[pivot_idx]
    for i in range(len(data)):
        if i != pivot_idx:
            if data[i] < pivot_val:
                left.append(data[i])
            else:
                right.append(data[i])
    return left, right, pivot_val


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
    pivot = data[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if pivot > data[j]:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[i - 1], data[l] = data[l], data[i - 1]
    return i - 1


if __name__ == "__main__":
    data = [30, 2, 10, 100, 24, 7, 79]
    print('org:', data)
    print('sorted:', quick_sort(data))

    data = [30, 2, 10, 100, 24, 7, 79]
    print('sorted(in place):', quick_sort_in_place(data))