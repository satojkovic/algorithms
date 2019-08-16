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