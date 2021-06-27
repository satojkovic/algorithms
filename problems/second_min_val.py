class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def second_min_val(root):
    import sys
    uniq_nodes = set()
    traverse(root, uniq_nodes)
    min_val = root.val
    next_min = sys.maxsize
    for node in uniq_nodes:
        if min_val < node < next_min:
            next_min = node
    return next_min if next_min < sys.maxsize else -1


def traverse(root, uniq_nodes):
    if root:
        uniq_nodes.add(root.val)
        traverse(root.left, uniq_nodes)
        traverse(root.right, uniq_nodes)


def test_second_min_val():
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    assert second_min_val(root) == 5

    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    assert second_min_val(root) == -1

    root = TreeNode(123)
    assert second_min_val(root) == -1
