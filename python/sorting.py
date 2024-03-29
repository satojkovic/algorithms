#!/usr/bin/env python
# -*- coding=utf-8 -*-

# time complexity: O(n^2)
# space complexity: O(1)
# not stable
def selection_sort(data):
    for i in range(len(data)-1):
        min_idx = i
        # Find minimum
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        # Swap i-th element with minimum
        data[i], data[min_idx] = data[min_idx], data[i]
        print(data)
    return data


def test_selection_sort():
    assert selection_sort([3, 1, 10, 7, 6]) == [1, 3, 6, 7, 10]
    assert selection_sort([2, 2, 2]) == [2, 2, 2]
    assert selection_sort([23, -1]) == [-1, 23]
    assert selection_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert selection_sort([]) == []


# recursive version
def selection_sort_r(data):
    def find_min_idx(data, start):
        min_pos = start
        for i in range(start + 1, len(data)):
            if data[min_pos] > data[i]:
                min_pos = i
        return min_pos

    def _selection_sort_r(data, start):
        # base case: when start become (len(data) - 1)
        if start < len(data) - 1:
            min_pos = find_min_idx(data, start)
            data[start], data[min_pos] = data[min_pos], data[start]
            _selection_sort_r(data, start + 1)
        return data

    return _selection_sort_r(data, 0)


def selection_sort_stable(data):
    def insert(data, i):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        val = data[min_idx]
        for k in range(min_idx, i, -1):
            data[k] = data[k - 1]
        data[i] = val
        return data

    if data is None:
        return None

    for i in range(len(data) - 1):
        data = insert(data, i)
        print(data)
    return data


# worst case: O(n^2)
# average case: O(n^2)
# best case: O(n)
# Note: stable and in-place
def insertion_sort(data):
    for i in range(1, len(data)):
        pivot = data[i]
        # Repeat until the pivot is greater than data[j]
        j = i
        while j > 0:
            if data[j - 1] > pivot:
                data[j] = data[j - 1]
                j -= 1
            else:
                break
        data[j] = pivot
    return data

def test_insertion_sort():
    assert insertion_sort([4, 1, 3, 5, 2]) == [1, 2, 3, 4, 5]
    assert insertion_sort([1, 3, 1]) == [1, 1, 3]
    assert insertion_sort([10]) == [10]
    assert insertion_sort([10, 20, 30]) == [10, 20, 30]
    assert insertion_sort([]) == []


# worst case = pivotがsmallestもしくはlargetstなとき
#   分割後が1ずつ少なくなりながら比較, n-1 + n-2 + n-3 + ... + 2 + 1 = o(n^2)
# best case = pivotがmediumなとき
#   分割の回数は2分割していってleafが全て1になったとき => logn
#   比較回数は各深さで合計するとnなので、O(nlogn)
# average caseも同様に、O(nlogn)
#
# leftとrightがleafのときにはlogn必要 => O(logn)
#
# not stable sort
def quick_sort(data):
    if len(data) < 2:
        return data
    pivot = data[len(data) // 2]
    left, right, equal = [], [], []
    for d in data:
        if d < pivot: left.append(d)
        elif d == pivot: equal.append(d)
        else: right.append(d)
    return quick_sort(left) + equal + quick_sort(right)


def quick_sort_in_place(data):
    """quick sort in place partition

    Args:
        data (list): an input list

    Returns:
        list: a sorted list
    """
    def _quick_sort(data, l, r):
        if l > r:
            return
        mid = partition(data, l, r)
        _quick_sort(data, l, mid - 1)
        _quick_sort(data, mid + 1, r)
        return data
    return _quick_sort(data, 0, len(data) - 1) if len(data) > 0 else []


def partition(data, l, r):
    # m indicate the tail position of lesser elements
    m = l
    for i in range(l + 1, r + 1):
        if data[i] <= data[l]:
            m += 1
            data[i], data[m] = data[m], data[i]
    data[l], data[m] = data[m], data[l]
    return m


def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        # Use '<=' so as to be stable in the order
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    # Append what is remained in either of the lists
    return merged + left[left_idx:] + right[right_idx:]

# Time complexity: O(nlogn)
# Space complexity: O(n)
def merge_sort(data):
    # base case or data is empty
    if len(data) <= 1:
        return data

    # Split the data until reaching the base case
    mid_idx = len(data) // 2
    left = merge_sort(data[:mid_idx])
    right = merge_sort(data[mid_idx:])

    # Sort and Merge
    merged = merge(left, right)
    return merged


def heapify(data, i, n):
    # 親ノードをlargestと仮定
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # leftとrightがnを超えないようにチェックしながら
    # largestが親ノードでなくなるまで(base case)行う
    if l <= n and data[largest] < data[l]:
        largest = l
    if r <= n and data[largest] < data[r]:
        largest = r

    # not base case = recursive case
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        data = heapify(data, largest, n)

    return data

# O(nlogn) time, O(1) space
#
# data全体のheapifyでは、dataの半分の繰り返しが行われる(親ノードpから始まる)
# 各繰り返しにおいては、最大でtreeの深さ分(logn)の繰り返しheapifyが行われる
# したがって (n/2) * logn
#
# sort stageでは、n-1回の繰り返しで各繰り返しで同様に
# 最大でtreeの高さ分(logn)の繰り返しが発生し、nlogn
#
def heap_sort(data):
    if data is None:
        return None

    last_idx = len(data) - 1
    last_pidx = last_idx // 2 if last_idx % 2 != 0 else last_idx // 2 - 1

    # data全体をheap構造化
    for p in range(last_pidx, -1, -1):
        data = heapify(data, p, last_idx)
    print('heapified:', data)
    
    # 最大値をheapのroot（配列の先頭）から取り出して最後尾と交換
    # 交換すると残りのheap構造が崩れるので再度heapify
    # 以降は繰り返し
    for i in range(last_idx, 0, -1):
        data[i], data[0] = data[0], data[i]
        data = heapify(data, 0, i - 1)

    return data


