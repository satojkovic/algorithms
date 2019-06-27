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
    def __init__(self, capacity=3, load_factor=0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None for _ in range(self.capacity)]
        self.threshold = int(self.capacity * self.load_factor)

    def is_empty(self):
        return self.size == 0

    def insert(self, key, value):
        if key is None:
            return False
        bucket_index = self._get_index(key)
        return self._insert_entry(bucket_index, key, value)

    def remove(self, key):
        if key is None:
            return False
        bucket_index = self._get_index(key)
        value = self._remove_entry(bucket_index, key)
        if value:
            self.size -= 1
        return value

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

    def _remove_entry(self, bucket_index, key):
        if not self.table[bucket_index]:
            return None

        head = self.table[bucket_index]
        if head.key == key:
            return self._remove_first(bucket_index, key)

        target = head.next
        while target:
            if target.key == key:
                value = target.value
                head.next = target.next
                return value
            target = target.next
            head = head.next
        return None

    def _remove_first(self, bucket_index, key):
        if not self.table[bucket_index]:
            return None

        head = self.table[bucket_index]
        value = head.value
        self.table[bucket_index] = head.next
        return value

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

    def insert(self, key, value):
        if key is None:
            return None
        if self.used_buckets >= self.threshold:
            self._resize_table()

        # Searching for an empty bucket
        x = 1
        key_hash = hash(key)
        index = self._get_index(key_hash)
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
            index = self._get_index(key_hash + self._quad_probing(x))
            x += 1

    def remove(self, key):
        if key is None:
            return None

        x = 1
        key_hash = hash(key)
        index = self._get_index(key_hash)
        while True:
            # Ignore deleted buckets
            if self.key_table[index] == self.tombstone:
                index = self._get_index(key_hash + self._quad_probing(x))
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
        index = self._get_index(key_hash)
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

            index = self._get_index(key_hash + self._quad_probing(x))
            x += 1

    def print_table(self):
        for i, (key, value) in enumerate(zip(self.key_table, self.value_table)):
            print('[bucket {}] {} => {}'.format(i, key, value))

    def _quad_probing(self, x):
        return (x**2 + x) >> 1

    def _get_index(self, key):
        return (key & 0x7fffffff) % self.capacity

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
                self.insert(key, old_value_table[i])
            old_key_table[i] = None
            old_value_table[i] = None

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

    print('remove:')
    ht.remove('ken')
    ht.print_table()
    print('remove:')
    ht.remove('william')
    ht.print_table()
    print('remove:')
    ht.remove('bob')
    ht.print_table()
    print('remove:')
    if not ht.remove('arnold'):
        print('Not found: arnold')

    print()
    ht_qp = HashTableQuadProbing()
    print('Init:')
    ht_qp.print_table()
    print('insert:')
    ht_qp.insert('william', 21)
    ht_qp.print_table()
    print('Insert:')
    ht_qp.insert('bob', 40)
    ht_qp.print_table()
    print('Insert:')
    ht_qp.insert('ken', 11)
    print('Insert:')
    ht_qp.insert('jones', 90)
    ht_qp.print_table()
    print('remove:')
    ht_qp.remove('william')
    ht_qp.print_table()
    print('remove:')
    ht_qp.remove('ken')
    ht_qp.print_table()
    print('remove:')
    ht_qp.remove('bob')
    ht_qp.print_table()
    print('remove:')
    if not ht_qp.remove('bob'):
        print('Not found')
    else:
        ht_qp.print_table()
    print('get:')
    print('jones =>', ht_qp.get('jones'))
    print('get:')
    print('tom =>', ht_qp.get('tom'))