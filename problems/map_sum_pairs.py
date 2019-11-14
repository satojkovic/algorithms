class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}

class MapSum1:
    def __init__(self):
        self.root = TrieNode(0)

    def insert(self, key, val):
        head = self.root
        self.insert_key_val(head, key, val)

    def insert_key_val(self, head, key, val):
        if len(key) == 1:
            if not key in head.children:
                head.children[key] = TrieNode(val)
            else:
                head.children[key].val = val
            return head

        if not key[0] in head.children:
            head.children[key[0]] = TrieNode(0)
        node = self.insert_key_val(head.children[key[0]], key[1:], val)
        head.children[key[0]] = node
        return head

    def sum(self, prefix):
        head = self.root
        head = self.search_prefix_head(head, prefix)
        return self.sum_val(head) if head else 0

    def sum_val(self, head):
        if len(head.children.keys()) == 0:
            return head.val
        res = head.val
        for c in head.children.keys():
            res += self.sum_val(head.children[c])
        return res

    def search_prefix_head(self, head, prefix):
        if len(prefix) == 0:
            return head
        if not prefix[0] in head.children:
            return None
        return self.search_prefix_head(head.children[prefix[0]], prefix[1:])

