def invert_binary_tree(root):
    if root is None:
        return None
    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)
    return root

def invertTree(root):
    if not root:
        return None
    inverted_left = invertTree(root.left)
    inverted_right = invertTree(root.right)
    root.left, root.right = inverted_right, inverted_left
    return root
