class TrieNode:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.word_finished = False


class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, s):
        def _insert(root, s, pos):
            if len(s) - 1 == pos:
                if not s[pos] in root.children:
                    root.children[s[pos]] = TrieNode(root.data + s[pos])
                root.children[s[pos]].word_finished = True
                return root

            if not s[pos] in root.children:
                root.children[s[pos]] = TrieNode(root.data + s[pos])
            root.children[s[pos]] = _insert(root.children[s[pos]], s, pos + 1)
            return root
        self.root = _insert(self.root, s, 0)

    def replace_with_prefix(self, word):
        head = self.root
        return self._replace_with_prefix(head, word)

    def _replace_with_prefix(self, head, word):
        if len(word) == 0 or head.word_finished:
            return head.data
        if not word[0] in head.children:
            return None
        return self._replace_with_prefix(head.children[word[0]], word[1:])


def replace_words(dict, sentence):
    trie = Trie()
    [trie.insert(word) for word in dict]
    res = []
    for word in sentence.split(' '):
        replaced_word = trie.replace_with_prefix(word)
        if replaced_word:
            res.append(replaced_word)
        else:
            res.append(word)
    return ' '.join(res)
