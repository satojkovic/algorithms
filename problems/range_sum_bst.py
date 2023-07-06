class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def range_sum_bst(root, low, high):
    if root is None:
        return 0
    sum = root.val if low <= root.val <= high else 0
    sum += range_sum_bst(root.left, low, high)
    sum += range_sum_bst(root.right, low, high)
    return sum


def test_range_sum_bst():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    assert range_sum_bst(root, 7, 15) == 32
    assert range_sum_bst(root, 1, 2) == 0
    assert range_sum_bst(root, 20, 30) == 0
    assert range_sum_bst(root, 3, 18) == 58

    root = None
    assert range_sum_bst(root, 7, 15) == 0
