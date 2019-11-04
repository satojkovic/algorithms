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

    merged = []
    left_idx = 0
    right_idx = 0

    # Find the next largest value between left and right
    # and adding that to the result list
    while left_idx < len(left) and right_idx < len(right):
        # Use '<=' so as to be stable in the order
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    # Append remaining elements to the result list
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged


def merge_sort(data):
    # base case or data is empty
    if len(data) <= 1:
        return data

    # [divide]
    # Split the data until reaching the base case
    mid_idx = len(data) // 2
    left = merge_sort(data[:mid_idx])
    right = merge_sort(data[mid_idx:])

    # [conquer]
    # Sort and merge
    merged = merge(left, right)
    return merged

if __name__ == "__main__":
    data = [1, 1, 5, -1, 8, 19, 2, 7]
    print('input:', data)
    print('--merge sort--')
    print('result:', merge_sort(data))
