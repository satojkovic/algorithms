class TrieNode:
    def __init__(self, data):
        self.data = data
        self.children = {}

def insert(root, s):
    if len(s) == 1:
        root.children[s] = TrieNode(root.data + s)
        return root

    if not root.children.get(s[0]):
        root.children[s[0]] = TrieNode(root.data + s[0])
    child = insert(root.children[s[0]], s[1:])
    root.children[s[0]] = child
    return root

def search(root, s):
    if len(s) == 0:
        return True
    if not s[0] in root.children:
        return False
    return search(root.children[s[0]], s[1:])