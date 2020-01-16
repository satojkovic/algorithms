class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)