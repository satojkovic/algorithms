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

def inorder_successor_iter(root, p):
    if p is not None and p.right:
        curr = p.right
        while curr.left:
            curr = curr.left
        return curr

    s = []
    curr = root
    prev = None
    while True:
        if curr is not None:
            s.append(curr)
            curr = curr.left
        elif s:
            node = s.pop()
            if prev is not None and prev.val == p.val:
                return node
            prev = node
            curr = node.right
        else:
            break
    return None
