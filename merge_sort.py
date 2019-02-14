#!/usr/bin/env python
# -*- coding=utf-8 -*-

def merge(left, right):
    """merge two sorted list
    
    Args:
        left ([list]): [a sorted list]
        right ([list]): [a sorted list]
    
    Returns:
        [list]: a merged list
    """

    sorted_data = []
    left_idx = 0
    right_idx = 0

    # find the next largest value between left and right,
    # and adding that to sorted_data
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_data.append(left[left_idx])
            left_idx += 1
        else:
            sorted_data.append(right[right_idx])
            right_idx += 1
    
    # append remaining elements to sorted_data
    if left_idx != len(left):
        sorted_data.extend(left[left_idx:])
    if right_idx != len(right):
        sorted_data.extend(right[right_idx:])

    return sorted_data


def merge_sort(data):
    # base case
    if len(data) < 2:
        return data

    # [split phase]
    # continue to split until reaching the base case
    mid_idx = len(data) // 2
    left = merge_sort(data[:mid_idx])
    right = merge_sort(data[mid_idx:])

    # [merge phase]
    merged = merge(left, right)
    return merged

if __name__ == "__main__":
    data = [1, 1, 5, -1, 8, 19, 2, 7]
    print('input:', data)
    print('--merge sort--')
    print('result:', merge_sort(data))
