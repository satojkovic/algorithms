from typing import List, Optional
from collections import deque
from tree_common import TreeNode, build_tree


def validate_bst(root):
    def validate(root, low=-float('inf'), high=float('inf')):
        if not root:
            return True

        if not (low < root.val < high):
            return False
        return validate(root.left, low, root.val) and validate(root.right, root.val, high)

    return validate(root)


def test_valid_bst():
    root = build_tree([2,1,3])
    assert validate_bst(root) is True

    root = build_tree([5,1,4,None,None,3,6])
    assert validate_bst(root) is False
