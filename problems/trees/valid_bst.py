from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(lst: List[Optional[int]]) -> Optional[TreeNode]:
    if not lst or lst[0] is None:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1

    while queue and i < len(lst):
        node = queue.popleft()

        # 左の子ノード
        if i < len(lst):
            if lst[i] is not None:
                node.left = TreeNode(lst[i])
                queue.append(node.left)
            i += 1

        # 右の子ノード
        if i < len(lst):
            if lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            i += 1

    return root


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
