#!/usr/bin/env python
# -*- coding=utf-8 -*-

class Array:
    def __init__(self, capacity=16):
        if capacity < 0:
            self.capacity = 16
        else:
            self.capacity = capacity
        self.arr = [0] * capacity
        self.length = 0

    def size(self):
        return self.length

    def is_empty(self):
        return self.size() == 0

    def clear(self):
        for i in range(self.capacity):
            self.arr[i] = 0
        self.length = 0

    def add(self, elem):
        if self.length + 1 >= self.capacity:
            # double the size
            self.capacity = 1 if self.capacity == 0 else self.capacity * 2
            new_arr = [0] * self.capacity
            for i in range(self.length):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
        self.arr[self.length] = elem
        self.length += 1

    def remove(self, target):
        if self.is_empty():
            return None
        # loop through each list element, O(n)
        j = 0
        new_arr = [0] * (self.capacity - 1)
        for i in range(self.length):
            if self.arr[i] != target:
                new_arr[j] = self.arr[i]
                j += 1
        self.arr = new_arr
        self.length -= 1
        self.capacity -= 1
        return True

    def print_list(self):
        if self.is_empty():
            print('List is empty')
            return
        print('Real elements:', end=' ')
        for i in range(self.length):
            print(self.arr[i], end=' ')
        print()

if __name__ == "__main__":
    myarr = Array()
    print('(size, capacity): {} {}'.format(myarr.length, myarr.capacity))

    num_elems = myarr.capacity + 1
    print('add {} elements'.format(num_elems))
    [myarr.add(i) for i in range(num_elems)]
    print('(size, capacity): {} {}'.format(myarr.length, myarr.capacity))
    myarr.print_list()

    target = 5
    print('remove {}'.format(target))
    myarr.remove(target)
    print('(size, capacity): {} {}'.format(myarr.length, myarr.capacity))
    myarr.print_list()

    target = 3
    print('remove {}'.format(target))
    myarr.remove(target)
    print('(size, capacity): {} {}'.format(myarr.length, myarr.capacity))
    myarr.print_list()