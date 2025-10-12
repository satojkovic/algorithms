class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end_of_word if curr.end_of_word else False

    def starts_with(self, s):
        curr = self.root
        for c in s:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

# test cases
def test_trie():
    trie = Trie()
    trie.insert("hello")
    assert trie.search("hello") == True
    assert trie.search("hell") == False
    assert trie.starts_with("he") == True
