class TrieNode:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.word_finished = False

def insert(root, s):
    if len(s) == 1:
        if not s in root.children:
            root.children[s] = TrieNode(root.data + s)
        root.children[s].word_finished = True
        return root

    if not s[0] in root.children:
        root.children[s[0]] = TrieNode(root.data + s[0])
    child = insert(root.children[s[0]], s[1:])
    root.children[s[0]] = child
    return root

def search(root, s):
    if len(s) == 0:
        return True if root.word_finished else False
    if not s[0] in root.children:
        return False
    return search(root.children[s[0]], s[1:])