#!/usr/bin/env python
# -*- coding=utf-8 -*-

def heapify(data, p):
    left_idx = 2 * p + 1
    right_idx = 2 * p + 2
    largest = p

    if left_idx < len(data) and data[largest] < data[left_idx]:
        largest = left_idx
    if right_idx < len(data) and data[largest] < data[right_idx]:
        largest = right_idx

    if largest != p:
        data[largest], data[p] = data[p], data[largest]
        print(data)
        data = heapify(data, largest)
    
    return data


def do_heapify(data):
    last_idx = len(data) - 1
    last_pidx = last_idx // 2 if last_idx % 2 != 0 else last_idx // 2 - 1
    for p in range(last_pidx, -1, -1):
        print('parent:', data[p])
        data = heapify(data, p)
    return data 


if __name__ == "__main__":
    data = [6, 5, 1, 8, 2, 4]
    data = do_heapify(data)
    print(data)
