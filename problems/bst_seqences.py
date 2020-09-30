import itertools

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bst_sequences(root):
    if root is None:
        return [[]]
    left = bst_sequences(root.left)
    right = bst_sequences(root.right)
    res = []
    for l, r in itertools.product(left, right):
        res += weave(l, r, [root.val])
    return res

def weave(left, right, prefix):
    if len(left) == 0 or len(right) == 0:
        return [prefix + left + right]
    res = []
    res += weave(left[1:], right, prefix + [left[0]])
    res += weave(left, right[1:], prefix + [right[0]])
    return res
