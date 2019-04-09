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

    def remove_at(self, rm_index):
        if rm_index >= self.length and rm_index < 0:
            return None
        # return value
        ret = self.arr[rm_index]
        j = 0
        new_arr = [0] * (self.length - 1)
        for i in range(self.length):
            if i == rm_index:
                j -= 1
            else:
                new_arr[j] = self.arr[i]
                j += 1
        self.arr = new_arr
        self.length -= 1
        self.capacity = self.length
        return ret

    def remove(self, elem):
        for i, d in enumerate(self.arr):
            if d == elem:
                self.remove_at(i)
                return True
        return False


if __name__ == "__main__":
    myarr = Array()
    print('(size, capacity): {} {}'.format(myarr.length, myarr.capacity))

    num_elems = myarr.capacity + 1
    print('add {} elements'.format(num_elems))
    [myarr.add(i) for i in range(num_elems)]
    print('(size, capacity): {} {}'.format(myarr.length, myarr.capacity))

    target = 5
    print('remove {}'.format(target))
    myarr.remove(target)
    print('(size, capacity): {} {}'.format(myarr.length, myarr.capacity))

    target = 3
    print('remove {}'.format(target))
    myarr.remove(target)
    print('(size, capacity): {} {}'.format(myarr.length, myarr.capacity))