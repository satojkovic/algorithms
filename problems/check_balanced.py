class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_balanced(root):
    if root is None:
        return True
    height_diff = get_height(root.left) - get_height(root.right)
    if height_diff > 1:
        return False
    else:
        return check_balanced(root.left) and check_balanced(root.right)


def get_height(root):
    if root is None:
        return -1
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    return max(left_height, right_height) + 1


def is_balanced(root):
    def _is_balanced(root):
        if root is None:
            return True, -1
        left_cond, left_h = _is_balanced(root.left)
        right_cond, right_h = _is_balanced(root.right)
        return abs(left_h - right_h) <= 1 and left_cond and right_cond, max(left_h, right_h) + 1
    cond, h = _is_balanced(root)
    return cond


def test_is_balanced():
    root = TreeNode(10)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    root.left.left = TreeNode(14)
    cond = is_balanced(root)
    assert cond == True

    root = TreeNode(10)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    cond = is_balanced(root)
    assert cond == False
