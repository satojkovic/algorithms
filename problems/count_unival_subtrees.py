class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def count_unival_subtrees(root):
    def _count_unival_subtrees(root):
        if root is None:
            return 0, []
        nl, left = _count_unival_subtrees(root.left)
        nr, right = _count_unival_subtrees(root.right)
        children = left + right
        total = nl + nr
        if len(children) == 0:
            total += 1
        elif root.val in set(children) and len(set(children)) == 1:
            total += 1
        return total, children + [root.val]
    n, _ = _count_unival_subtrees(root)
    return n