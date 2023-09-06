class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_leaves(root):
    res = []

    def find_leaves_with_sort_by_height(root, height):
        if root is None:
            return -1
        left = find_leaves_with_sort_by_height(root.left, height + 1)
        right = find_leaves_with_sort_by_height(root.right, height + 1)
        current = max(left, right) + 1
        if len(res) != 0 and current < len(res):
            res[current].append(root.val)
        else:
            res.append([root.val])
        return current

    _ = find_leaves_with_sort_by_height(root, 0)
    return res


def test_find_leaves():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert find_leaves(root) == [[4, 5, 3], [2], [1]]

    root = TreeNode(1)
    assert find_leaves(root) == [[1]]
