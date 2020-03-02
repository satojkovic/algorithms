#!/usr/bin/env python
# -*- coding=utf-8 -*-

def search_2d_mat(mat, target):
    return binary_search_2d_mat(mat, target)

def binary_search_2d_mat(mat, target):
    ret = False
    for m in range(len(mat)):
        ret = True if binary_search_r(mat[m], target, 0, len(mat[m]) - 1) else ret
    return ret

def binary_search_r(data, target, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
    if data[mid] == target:
        return True
    elif data[mid] > target:
        return binary_search_r(data, target, left, mid - 1)
    else:
        return binary_search_r(data, target, mid + 1, right)

def binary_search(data, target):
    """binary search

    Args:
        data (list): input list (binary search works only on a sorted list)
        target (int): target value
    
    Returns:
        int: the index of the target value in the list
    """

    return _binary_search(data, target, 0, len(data) - 1)


def _binary_search(data, target, left, right):
    """binary search algorithm

    First, compare the target value with the element located at middle of the left and right bounds.
    If the target value is greater than the value at middle, increase the left bound, else decrease
    the right bound.
    Repeat this process recursively until left bound is greater than right bound.
    If the target value equal the value at middle, we return the index of middle.
    If the target value is not present in the list, we return -1.
    
    Args:
        data (list): input list
        target (int): target value
        left (int): left bound of the input list
        right (int): right bound of the input list
    
    Returns:
        int: the index of the target value in the list
    """

    if left > right:
        return -1

    mid = (left + right) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return _binary_search(data, target, left, mid - 1)
    else:
        return _binary_search(data, target, mid + 1, right)

def binary_search_iter(data, target):
    lo = 0
    hi = len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == target:
            return mid
        elif target < data[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

if __name__ == "__main__":
    data = [1, 3, 4, 13, 40, 193]
    target = 40
    print('org:', data)
    result = binary_search(data, target)
    if result != -1:
        print('target {} is present at index {}'.format(target, result)) 
    else:
        print('target {} is not present in the list'.format(target))