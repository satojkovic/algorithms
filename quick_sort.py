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
        list: a sorted list
    """

    if len(data) < 2:
        return data

    pivot_idx = len(data) // 2
    pivot_val = data[pivot_idx]
    left, right = [], []
    for i in range(len(data)):
        if data[i] < pivot_val:
            left.append(data[i])
        elif data[i] > pivot_val:
            right.append(data[i])

    left = quick_sort(left)
    right = quick_sort(right)
    return left + [pivot_val] + right


if __name__ == "__main__":
    data = [30, 2, 10, 100, 24, 7, 79]
    print('org:', data)
    print('sorted:', quick_sort(data))