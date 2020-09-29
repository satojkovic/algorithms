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
        if len(l) == 0 and len(r) == 0:
            res.append([root.val])
        elif len(l) == 0:
            res.append([root.val] + r)
        elif len(r) == 0:
            res.append([root.val] + l)
        else:
            res.append([root.val] + l + r)
            res.append([root.val] + r + l)
    return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.right = TreeNode(9)
    root.right.left = TreeNode(8)
    root.right.right = TreeNode(11)

    print(bst_sequences(root))