class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(inorder, postorder):
    def _build_tree(root, inorder, postorder):
        if len(inorder) == 0 and len(postorder) == 0:
            return None
        if len(inorder) == 1 and len(postorder) == 1:
            return TreeNode(inorder[0])

        if root is None:
            root = TreeNode(postorder[-1])
        parent = postorder[-1]
        parent_idx = inorder.index(parent)
        root.left = _build_tree(
            root.left, inorder[:parent_idx], postorder[:len(inorder[:parent_idx])])
        root.right = _build_tree(
            root.right, inorder[parent_idx + 1:], postorder[len(postorder) - len(inorder[parent_idx + 1:]) - 1: -1])
        return root
    root = TreeNode(postorder[-1])
    return _build_tree(root, inorder, postorder)