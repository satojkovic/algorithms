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
    if len(postorder) == 0:
        return None
    return _build_tree(None, inorder, postorder)

def build_tree2(inorder, postorder):
    def _build_tree(root, inorder, postorder, left_in, right_in, left_post, right_post):
        if right_in < 0 or left_in >= len(inorder) or left_in > right_in:
            return None
        if left_in == right_in:
            return TreeNode(inorder[left_in])
        if root is None:
            root = TreeNode(postorder[right_post])
        parent_idx = inorder.index(postorder[right_post])
        left_len = parent_idx - left_in
        right_len = right_in - parent_idx
        root.left = _build_tree(
            root.left, inorder, postorder, left_in, parent_idx - 1, 
            left_post, left_post + left_len - 1)
        root.right = _build_tree(
            root.right, inorder, postorder, parent_idx + 1, right_in,
            left_post + left_len, left_post + left_len + right_len - 1
        )
        return root
    if len(postorder) == 0:
        return None
    return _build_tree(None, inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)