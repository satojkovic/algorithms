class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def check_subtree(T1, T2):
    if T1 is None or T2 is None:
        return False

    if T1.val == T2.val and check(T1, T2):
        return True

    return check_subtree(T1.left, T2) or check_subtree(T1.right, T2)

def check(T1, T2):
    if T1 is None and T2 is None:
        return True
    if T1 is None or T2 is None or T1.val != T2.val:
        return False
    return check(T1.left, T2.left) and check(T1.right, T2.right)

if __name__ == "__main__":
    root = TreeNode(11)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.right.right = TreeNode(6)
    root.right.right.left = TreeNode(7)

    root2 = TreeNode(8)
    root2.right = TreeNode(6)
    root2.right.left = TreeNode(7)

    root3 = TreeNode(4)
    root3.left = TreeNode(20)

    print(check_subtree(root, root2))
    print(check_subtree(root, root3))