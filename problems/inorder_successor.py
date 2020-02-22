class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_successor(root, p):
    inorder = inorder_traverse(root)
    return inorder[inorder.index(p) + 1] if len(inorder) != 0 and inorder.index(p) < len(inorder) - 1 else None

def inorder_traverse(root):
    if root is None:
        return []
    left = inorder_traverse(root.left)
    right = inorder_traverse(root.right)
    return left + [root] + right
