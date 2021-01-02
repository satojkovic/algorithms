#!/usr/bin/env python
# -*- coding=utf-8 -*-

class TombStone:
    pass

class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=1000, load_factor=0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.bucket = self.capacity * [None]
        self.threshold = int(self.capacity * self.load_factor)

    def _map_bucket_idx(self, key):
        return hash(key) % self.capacity

    def _bucket_seek(self, idx, key):
        head = self.bucket[idx]
        pos = 0
        while head:
            if head.key == key:
                return pos
            head = head.next
            pos += 1
        return -1

    def add(self, key, value):
        idx = self._map_bucket_idx(key)
        pos = self._bucket_seek(idx, key)
        if pos < 0:
            node = HashEntry(key, value)
            node.next = self.bucket[idx]
            self.bucket[idx] = node
            self.size += 1
        else:
            # Update the existing value
            head = self.bucket[idx]
            while pos > 0:
                head = head.next
                pos -= 1
            head.value = value

        if self.size > self.threshold:
            self._resize_table()

    def remove(self, key):
        idx = self._map_bucket_idx(key)
        head = self.bucket[idx]
        if head is None:
            return None
        if head.key == key:
            self.bucket[idx] = head.next
            self.size -= 1
            return key
        while head.next and head.next.key != key:
            head = head.next
        if head is None:
            return None
        else:
            head.next = head.next.next
            self.size -= 1
            return key

    def get(self, key):
        idx = self._map_bucket_idx(key)
        pos = self._bucket_seek(idx, key)
        if pos < 0:
            return None
        else:
            head = self.bucket[idx]
            while pos > 0:
                head = head.next
                pos -= 1
            return head.value

    def _resize_table(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * self.load_factor)
        new_bucket = self.capacity * [None]

        for bucket in self.bucket:
            if bucket is None:
                continue
            head = bucket
            while head:
                idx = self._map_bucket_idx(head.key)
                if new_bucket[idx]:
                    node = HashEntry(head.key, head.value)
                    node.next = new_bucket[idx]
                    new_bucket[idx] = node
                else:
                    new_bucket[idx] = HashEntry(head.key, head.value)
                head = head.next
        self.bucket = new_bucket

    def print_table(self):
        print('(capacity, size, threshold) = ({}, {}, {}):'.format(self.capacity, self.size, self.threshold))
        for i, bucket in enumerate(self.bucket):
            print('[bucket {}]'.format(i), end=' ')
            head = bucket
            while head:
                print('{} => {}'.format(head.key, head.value), end=' ')
                head = head.next
            print()

class HashTableQuadProbing:
    def __init__(self, capacity=8, load_factor=0.45):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.key_table = [None for _ in range(self.capacity)]
        self.value_table = [None for _ in range(self.capacity)]
        self.threshold = int(self.capacity * self.load_factor)
        self.used_buckets = 0
        self.key_count = 0
        self.tombstone = TombStone()

    def add(self, key, value):
        if key is None:
            return None
        if self.used_buckets >= self.threshold:
            self._resize_table()

        # Searching for an empty bucket
        x = 1
        key_hash = hash(key)
        index = self._map_bucket_idx(key_hash)
        seen_tombstone = -1
        while True:
            # The current bucket was previously deleted
            if self.key_table[index] == self.tombstone:
                if seen_tombstone == -1:
                    seen_tombstone = index
            elif self.key_table[index] is not None:
                if self.key_table[index] == key:
                    old_value = self.value_table[index]
                    if seen_tombstone == -1:
                        self.value_table[index] = value
                    else:
                        self.key_table[index] = self.tombstone
                        self.value_table[index] = None
                        self.key_table[seen_tombstone] = key
                        self.value_table[seen_tombstone] = value
                    return old_value
            else:
                # No previously encountered deleted buckets
                if seen_tombstone == -1:
                    self.used_buckets += 1
                    self.key_count += 1
                    self.key_table[index] = key
                    self.value_table[index] = value
                else:
                    self.key_count += 1
                    self.key_table[seen_tombstone] = key
                    self.value_table[seen_tombstone] = value
                return None

            # Quadratic Probing
            index = self._map_bucket_idx(key_hash + self._quad_probing(x))
            x += 1

    def remove(self, key):
        if key is None:
            return None

        x = 1
        key_hash = hash(key)
        index = self._map_bucket_idx(key_hash)
        while True:
            # Ignore deleted buckets
            if self.key_table[index] == self.tombstone:
                index = self._map_bucket_idx(key_hash + self._quad_probing(x))
                x += 1
                continue

            # Key was not found in hash table
            if self.key_table[index] == None:
                return None

            # Target was found
            if self.key_table[index] == key:
                self.key_count -= 1
                old_value = self.value_table[index]
                self.key_table[index] = self.tombstone
                self.value_table[index] = None
                return old_value

    def get(self, key):
        if key is None:
            return None

        x = 1
        key_hash = hash(key)
        index = self._map_bucket_idx(key_hash)
        seen_tombstone = -1
        while True:
            if self.key_table[index] == self.tombstone:
                seen_tombstone = index
            elif self.key_table[index] != None:
                if seen_tombstone != -1:
                    # lazy deletion/relocation
                    self.key_table[seen_tombstone] = self.key_table[index]
                    self.value_table[seen_tombstone] = self.value_table[index]

                    self.key_table[index] = self.tombstone
                    self.value_table[index] = None
                    return self.value_table[seen_tombstone]
                else:
                    return self.value_table[index]
            else:
                # Not found
                return None

            index = self._map_bucket_idx(key_hash + self._quad_probing(x))
            x += 1

    def print_table(self):
        for i, (key, value) in enumerate(zip(self.key_table, self.value_table)):
            print('[bucket {}] {} => {}'.format(i, key, value))

    def _quad_probing(self, x):
        return (x**2 + x) >> 1

    def _map_bucket_idx(self, key):
        return hash(key) % self.capacity

    def _resize_table(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * self.load_factor)
        self.key_count = 0
        self.used_buckets = 0

        old_key_table = self.key_table
        self.key_table = [None for _ in range(self.capacity)]
        old_value_table = self.value_table
        self.value_table = [None for _ in range(self.capacity)]

        for i, key in enumerate(old_key_table):
            if old_key_table[i] != None and old_key_table[i] != self.tombstone:
                self.add(key, old_value_table[i])
            old_key_table[i] = None
            old_value_table[i] = None
