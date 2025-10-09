class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummy_head = DLLNode(None, None)
        self.dummy_tail = DLLNode(None, None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        org_first = self.dummy_head.next
        node.next = org_first
        node.prev = self.dummy_head
        self.dummy_head.next = node
        org_first.prev = node

    def _remove_from_tail(self):
        if len(self.cache) == 0:
            return None
        tail_node = self.dummy_tail.prev
        self._remove_node(tail_node)
        return tail_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._remove_node(self.cache[key])
        self._add_to_head(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_head(node)
        else:
            new_node = DLLNode(key, value)
            self._add_to_head(new_node)
            self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            lru_node = self._remove_from_tail()
            if lru_node:
                del self.cache[lru_node.key]

class DLLNode:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value


def test_lru_cache():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)
    assert lru.get(2) == -1
    lru.put(4, 4)
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4
