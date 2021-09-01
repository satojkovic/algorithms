class TrieNode:
    def __init__(self, val):
        self.val = val
        self.childs = {}
        self.is_end = False


def longest_common_prefix(strs):
    if not strs:
        return ''
    if len(strs) == 1:
        return strs[0]

    root = create_trie(strs[1:])
    res = []
    for c in strs[0]:
        if not c in root.childs or len(root.childs.keys()) != 1 or root.is_end:
            break
        res.append(c)
        root = root.childs[c]
    return ''.join(res)


def create_trie(strs):
    root = TrieNode(None)
    for s in strs:
        root = insert(root, s)
    return root


def insert(root, s):
    org_root = root
    for c in s:
        if not c in root.childs:
            root.childs[c] = TrieNode(c)
        root = root.childs[c]
    root.is_end = True
    return org_root


def test_longest_common_prefix():
    assert longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'
    assert longest_common_prefix(['', 'test']) == ''
    assert longest_common_prefix(['abc']) == 'abc'
    assert longest_common_prefix(['abc', 'bca', 'cab']) == ''
