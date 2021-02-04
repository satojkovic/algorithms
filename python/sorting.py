#!/usr/bin/env python
# -*- coding=utf-8 -*-

# O(n^2)
# i=0, 1, 2, ..., n-1の各要素で、
# n-1回の比較 + n-2回の比較 + ... + 1 = (n * (n-1) / 2)回の計算
#
# nによらず、i, j, min_idxが必要になるだけ => O(1) space
#
# stable
def selection_sort(data):
    if data is None:
        return None

    # i番目とj=i+1番目以降の要素を比較
    # data[i] > data[j]の中でminな要素とswap
    for i in range(len(data)-1):
        min_idx = i
        for j in range(i+1, len(data)):
            # i+1番目以降の要素でminな要素のindexに逐次更新
            if data[min_idx] > data[j]:
                min_idx = j
        # 最終的にmin_idxと現在のi番目の要素をswap
        data[i], data[min_idx] = data[min_idx], data[i]
        print(data)
    return data

# recursive
def do_selection_sort_r(data):
    return selection_sort_r(data, 0)

def selection_sort_r(data, start):
    # base caseはpivot位置が(len(data) - 1) - 1になるとき
    if start < len(data) - 1:
        min_pos = find_min_idx(data, start)
        data[start], data[min_pos] = data[min_pos], data[start]
        selection_sort_r(data, start + 1)
    return data


def selection_sort_stable(data):
    if data is None:
        return None

    for i in range(len(data) - 1):
        data = insert(data, i)
        print(data)
    return data


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


def find_min_idx(data, start):
    min_pos = start
    for i in range(start + 1, len(data)):
        if data[min_pos] > data[i]:
            min_pos = i
    return min_pos


# worst case: O(n^2)
# average case: O(n^2)
# best case: O(n)
# Note: stable and in-place
def insertion_sort(data):
    for i in range(1, len(data)):
        pivot = data[i]
        j = i - 1
        # Repeat until the pivot is greater than data[j]
        while j >= 0 and pivot < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = pivot
    return data


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


if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print('org', data)
    print('--selection sort--')
    print('result', selection_sort(data))

    data = [4, 3, 4, 2, 1]
    print('org', data)
    print('--selection sort stable--')
    print('result', selection_sort_stable(data))

    data = [64, 25, 12, 22, 11]
    print('--insertion sort--')
    print('result', insertion_sort(data))

    data = [64, 25, 12, 22, 11]
    print('--quick sort--')
    print('result', quick_sort(data))

    data = [97, 200, 100, 101, 211, 107]
    print('--quick sort in place--')
    print('result', quick_sort_in_place(data))

    data = [6, 5, 3, 1, 8, 7, 2, 4]
    print('org', data)
    print('--merge sort--')
    print('result', merge_sort(data))

    #data = [4, 1, 6, 2, 9, 7, 3, 8]
    data = [6, 5, 1, 8, 2, 4]
    print('org', data)
    print('heap sort')
    print('result', heap_sort(data))