#!/usr/bin/env python
# -*- coding=utf-8 -*-

def binary_search(data, target):
    def _binary_search(data, target, left, right):
        if left > right:
            return -1

        mid = left + (right - left) // 2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            return _binary_search(data, target, left, mid - 1)
        else:
            return _binary_search(data, target, mid + 1, right)

    return _binary_search(data, target, 0, len(data) - 1)


def binary_search_iter(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if data[mid] == target:
            return mid
        elif target < data[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binary_search_sparse(strs, s, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if strs[mid] == '':
        near_left = mid - 1
        near_right = mid + 1
        while True:
            if near_left < left and right < near_right:
                return -1
            elif left <= near_left and strs[near_left] != '':
                mid = near_left
            elif near_right <= right and strs[near_right] != '':
                mid = near_right
            near_left -= 1
            near_right += 1

    if strs[mid] == s:
        return mid
    elif s < strs[mid]:
        return binary_search_sparse(strs, s, left, mid - 1)
    else:
        return binary_search_sparse(strs, s, mid + 1, right)


def binary_search2(data, target):
    left, right = -1, len(data)
    while right - left > 1:
        mid = left + (right - left) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid
        else:
            right = mid
    return -1

def test_binary_search():
    data = [1, 3, 4, 13, 40, 193]
    assert binary_search(data, 40) == 4
    assert binary_search(data, 11) == -1
    assert binary_search(data, 1) == 0
    assert binary_search(data, 193) == 5


def test_binary_search_iter():
    data = [1, 3, 4, 13, 40, 193]
    assert binary_search_iter(data, 40) == 4
    assert binary_search_iter(data, 11) == -1
    assert binary_search_iter(data, 1) == 0
    assert binary_search_iter(data, 193) == 5
