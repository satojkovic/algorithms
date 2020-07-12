def invert_binary_tree(root):
    if root is None:
        return None
    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)
    return root