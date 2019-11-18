class TrieNode:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.word_finished = False

class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, s):
        root = self.root
        self._insert(root, s)

    def _insert(self, root, s):
        if len(s) == 1:
            if not s in root.children:
                root.children[s] = TrieNode(root.data + s)
            root.children[s].word_finished = True
            return root

        if not s[0] in root.children:
            root.children[s[0]] = TrieNode(root.data + s[0])
        child = self._insert(root.children[s[0]], s[1:])
        root.children[s[0]] = child
        return root

    def search(self, s):
        root = self.root
        return self._search(root, s)

    def _search(self, root, s):
        if len(s) == 0:
            return True if root.word_finished else False
        if not s[0] in root.children:
            return False
        return self._search(root.children[s[0]], s[1:])

    def starts_with(self, s):
        root = self.root
        return self._starts_with(root, s)

    def _starts_with(self, root, s):
        if len(s) == 0:
            return True
        if not s[0] in root.children:
            return False
        return self._starts_with(root.children[s[0]], s[1:])

    def _search_root(self, root, s):
        if len(s) == 0:
            return root
        if not s[0] in root.children:
            return None
        return self._search_root(root.children[s[0]], s[1:])

    def prefix_search(self, prefix):
        root = self.root
        root = self._search_root(root, prefix)
        return self._prefix_search(root) if root else []

    def _prefix_search(self, root):
        if len(root.children.keys()) == 0:
            return [root.data] if root.word_finished else []
        res = []
        if root.word_finished:
            res.append(root.data)
        for c in root.children.keys():
            res += self._prefix_search(root.children[c])
        return res