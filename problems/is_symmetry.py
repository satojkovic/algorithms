import pytest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Time complexity: O(n)
#
# Space complexity: O(n)
def is_symmetry1(root):
    if not root:
        return True
    q = []
    q.append([root.left, root.right])
    while q:
        t1, t2 = q.pop(0)
        if t1 is None and t2 is None:
            continue
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val:
            return False
        q.append([t1.left, t2.right])
        q.append([t1.right, t2.left])
    return True


@pytest.fixture
def symmetry_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    return root


@pytest.fixture
def asymmetry_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    return root


def test_is_symmetry(symmetry_tree, asymmetry_tree):
    assert is_symmetry1(symmetry_tree) is True
    assert is_symmetry1(asymmetry_tree) is False
    assert is_symmetry1(None) is True
