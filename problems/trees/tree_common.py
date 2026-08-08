from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

