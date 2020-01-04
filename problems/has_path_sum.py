class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def has_path_sum(root, path_sum):
    def _has_path_sum(root, path_sum, curr_sum):
        if root.left is None and root.right is None:
            return path_sum == curr_sum + root.val
        if root.left and _has_path_sum(root.left, path_sum, curr_sum + root.val):
            return True
        elif root.right and _has_path_sum(root.right, path_sum, curr_sum + root.val):
            return True
        else:
            return False
    return _has_path_sum(root, path_sum, 0) if root is not None else False
