class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_lowest_common_ancestor(root, p, q):
    if not root:
        return None

    if p.val < root.val and q.val < root.val:
        return find_lowest_common_ancestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return find_lowest_common_ancestor(root.right, p, q)

    return root


def find_lowest_common_ancestor_iterative(root, p, q):
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr
    return None


def test_find_lowest_common_ancestor():
    # Create a sample BST
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    p = root.left  # Node with value 2
    q = root.right  # Node with value 8
    assert find_lowest_common_ancestor(root, p, q).val == 6

    p = root.left  # Node with value 2
    q = root.left.right  # Node with value 4
    assert find_lowest_common_ancestor(root, p, q).val == 2

    p = root.left.right.left  # Node with value 3
    q = root.left.right.right  # Node with value 5
    assert find_lowest_common_ancestor(root, p, q).val == 4


def test_find_lowest_common_ancestor_iterative():
    # Create a sample BST
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    p = root.left  # Node with value 2
    q = root.right  # Node with value 8
    assert find_lowest_common_ancestor_iterative(root, p, q).val == 6

    p = root.left  # Node with value 2
    q = root.left.right  # Node with value 4
    assert find_lowest_common_ancestor_iterative(root, p, q).val == 2

    p = root.left.right.left  # Node with value 3
    q = root.left.right.right  # Node with value 5
    assert find_lowest_common_ancestor_iterative(root, p, q).val == 4
