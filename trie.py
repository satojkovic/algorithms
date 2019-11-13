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

def starts_with(root, s):
    if len(s) == 0:
        return True
    if not s[0] in root.children:
        return False
    return starts_with(root.children[s[0]], s[1:])

def search_head(root, s):
    if len(s) == 0:
        return root
    if not s[0] in root.children:
        return None
    return search_head(root.children[s[0]], s[1:])

def prefix_search(root, prefix):
    head = search_head(root, prefix)
    return prefix_search_cand(head) if head else []

def prefix_search_cand(head):
    if len(head.children.keys()) == 0:
        return [head.data] if head.word_finished else []
    res = []
    if head.word_finished:
        res.append(head.data)
    for c in head.children.keys():
        res += prefix_search_cand(head.children[c])
    return res