#!/usr/bin/env python
# -*- coding=utf-8 -*-

class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=3, load_factor=0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = self.capacity * [None]
        self.threshold = int(self.capacity * self.load_factor)

    def is_empty(self):
        return self.size == 0

    def insert(self, key, value):
        if key is None:
            return False
        bucket_index = self._get_index(key)
        return self._insert_entry(bucket_index, key, value)

    def print_table(self):
        print('(capacity, size, threshold) = ({}, {}, {}):'.format(self.capacity, self.size, self.threshold))
        for i, bucket in enumerate(self.table):
            print('[bucket {}]'.format(i), end=' ')
            head = bucket
            while head:
                print('{} => {}'.format(head.key, head.value), end=' ')
                head = head.next
            print()

    def _get_index(self, key):
        return (hash(key) & 0x7fffffff) % self.capacity

    def _add_last(self, bucket_index, key, value):
        bucket = self.table[bucket_index]
        if not bucket:
            self.table[bucket_index] = HashEntry(key, value)
            self.size += 1
            return

        head = bucket
        while head.next:
            head = head.next
        head.next = HashEntry(key, value)
        self.size += 1

    def _insert_entry(self, bucket_index, key, value):
        # exist_entry is None if same value doesn't exist in the bucket
        exist_entry = self._bucket_seek(bucket_index, key)
        if not exist_entry:
            # Append HashEntry
            self._add_last(bucket_index, key, value)
            if self.size > self.threshold:
                self._resize_table()
        else:
            # Update value
            exist_entry.value = value
        return

    def _resize_table(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * self.load_factor)
        new_table = self.capacity * [None]

        for bucket in self.table:
            if bucket:
                head = bucket
                while head:
                    bucket_index = self._get_index(head.key)
                    if new_table[bucket_index]:
                        new_table_head = new_table[bucket_index]
                        while new_table_head.next:
                            new_table_head = new_table_head.next
                        new_table_head.next = HashEntry(head.key, head.value)
                    else:
                        new_table[bucket_index] = HashEntry(head.key, head.value)
                    head = head.next
        self.table = new_table

    def _bucket_seek(self, bucket_index, key):
        if key is None:
            return None

        bucket = self.table[bucket_index]
        if not bucket:
            return None
        head = bucket
        while head:
            if head.key == key:
                return head
            head = head.next
        return None

    def _remove_first(self, bucket_index, key):
        if not self.table[bucket_index]:
            return None

        head = self.table[bucket_index]
        value = head.value
        self.table[bucket_index] = head.next
        return value

if __name__ == "__main__":
    ht = HashTable()
    print('Init:')
    ht.print_table()
    print('Insert:')
    ht.insert('william', 21)
    ht.print_table()
    print('Insert:')
    ht.insert('bob', 40)
    ht.print_table()
    print('Insert:')
    ht.insert('ken', 11)
    ht.print_table()
