class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False


def longest_common_prefix(strs):
    if len(strs) == 1:
        return strs[0]

    root = create_trie(strs[1:])
    return search(root, strs[0])


def create_trie(strs):
    root = TrieNode()
    for s in strs:
        root = insert(root, s)
    return root


def insert(root, s):
    org_root = root
    for c in s:
        if c not in root.child:
            root.child[c] = TrieNode()
        root = root.child[c]
    root.is_end = True
    return org_root


def search(root, s):
    res = []
    for c in s:
        if c not in root.child or len(root.child) != 1 or root.is_end:
            break
        res.append(c)
        root = root.child[c]
    return "".join(res)


def test_longest_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["", "test"]) == ""
    assert longest_common_prefix(["test", ""]) == ""
    assert longest_common_prefix(["abc"]) == "abc"
    assert longest_common_prefix(["abc", "bca", "cab"]) == ""


def longest_common_prefix2(strs):
    if not strs:
        return ''
    if len(strs) == 1:
        return strs[0]
    min_len = min([len(s) for s in strs])
    left, right = 0, min_len + 1  # [0, min_len + 1)
    while abs(right - left) > 1:
        mid = (left + right) // 2
        if is_common(strs, mid):
            left = mid
        else:
            right = mid
    return strs[0][:left]


def is_common(strs, mid):
    query_str = strs[0][:mid]
    for i in range(1, len(strs)):
        if query_str != strs[i][:mid]:
            return False
    return True


def test_longest_common_prefix2():
    assert longest_common_prefix2(['flower', 'flow', 'flight']) == 'fl'
    assert longest_common_prefix2(['', 'test']) == ''
    assert longest_common_prefix2(['abc']) == 'abc'
    assert longest_common_prefix2(['abc', 'bca', 'cab']) == ''
