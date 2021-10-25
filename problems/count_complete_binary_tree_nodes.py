def get_depth(root):
    d = 0
    while root.left:
        root = root.left
        d += 1
    return d


def get_num_last_d_nodes(root, d):
    max_num_nodes = 2 ** d
    left, right = 1, max_num_nodes - 1
    while left <= right:
        mid = left + (right - left) // 2
        if check(root, d, mid):
            left = mid + 1
        else:
            right = mid - 1
    return left


def check(root, d, mid):
    max_num_nodes = 2 ** d
    left, right = 0,  max_num_nodes - 1
    for _ in range(d):
        center = left + (right - left) // 2
        if mid <= center:
            root = root.left
            right = center
        else:
            root = root.right
            left = center + 1
    return root is not None


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_nodes(root):
    if root is None:
        return 0
    d = get_depth(root)
    if d == 0:
        return 1
    num_last_d_nodes = get_num_last_d_nodes(root, d)
    return 2 ** d - 1 + num_last_d_nodes


def test_count_nodes():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    assert count_nodes(root) == 6
    root = None
    assert count_nodes(root) == 0
    root = TreeNode(1)
    assert count_nodes(root) == 1
