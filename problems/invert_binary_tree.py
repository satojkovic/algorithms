def invert_binary_tree(root):
    if root is None:
        return None
    left = invert_binary_tree(root.right)
    right = invert_binary_tree(root.left)
    root.left = left
    root.right = right
    return root