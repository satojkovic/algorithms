class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


# Time complexity: O(n), visit each node exactly once
# Space complexity: O(n)(worst case: completely unbalanced), O(log(n))(best case: the height of the tree would be log(n))
def max_depth(root):
    if root is None:
        return 0
    left_height = max_depth(root.left)
    right_height = max_depth(root.right)
    return max(left_height, right_height) + 1

def max_depth_recursive(root):
    if not root:
        return 0
    return max(max_depth_recursive(root.left), max_depth_recursive(root.right)) + 1


def test_max_depth():
    root = TreeNode(3)
    root.left = TreeNode(10)
    root.right = TreeNode(1)
    root.right.left = TreeNode(32)
    assert max_depth(root) == 3

    root = None
    assert max_depth(root) == 0

    root = TreeNode(1)
    assert max_depth(root) == 1

def test_max_depth_recursive():
    root = TreeNode(3)
    root.left = TreeNode(10)
    root.right = TreeNode(1)
    root.right.left = TreeNode(32)
    assert max_depth_recursive(root) == 3

    root = None
    assert max_depth_recursive(root) == 0

    root = TreeNode(1)
    assert max_depth_recursive(root) == 1
