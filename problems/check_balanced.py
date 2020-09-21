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

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    root.left.left = TreeNode(14)

    print(check_balanced(root))