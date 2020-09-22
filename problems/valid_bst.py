class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def validate_bst(root):
    def _validate_bst(root, min_val, max_val):
        if root is None:
            return True
        # Being False if the current node is greater than or equal to the min_val or less than the max_val
        # Return immediately if the current node is not valid
        if (min_val is not None and min_val >= root.val) or (max_val is not None and max_val < root.val):
            return False
        # Check if the left branch and the right branch is valid
        # Return immediately if the left or right branch is not valid
        if not _validate_bst(root.left, min_val, root.val):
            return False
        if not _validate_bst(root.right, root.val, max_val):
            return False
        # Return True if all conditions are cleared
        return True
    return _validate_bst(root, None, None)

def validate_bst_i(root):
    if root is None:
        return True

    stack = [(root, None, None)]
    while stack:
        root, min_val, max_val = stack.pop()
        if root is None:
            continue
        if (min_val is not None and min_val >= root.val) or (max_val is not None and max_val < root.val):
            return False
        stack.append((root.left, min_val, root.val))
        stack.append((root.right, root.val, max_val))
    return True

def validate_bst_bf(root):
    is_valid, nodes = _validate_bst(root)
    return is_valid

def _validate_bst(root):
    if root is None:
        return True, []
    is_lvalid, left = _validate_bst(root.left)
    is_rvalid, right = _validate_bst(root.right)
    if is_lvalid and is_rvalid and validate(root, left, right):
        return True, left + [root.val] + right
    else:
        return False, left + [root.val] + right

def validate(root, left, right):
    for l in left:
        if l > root.val:
            return False
    for r in right:
        if r < root.val:
            return False
    return True

