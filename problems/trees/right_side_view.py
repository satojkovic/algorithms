from tree_common import TreeNode, build_tree
from typing import Optional, List
from collections import deque

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    out = []
    q = deque([root])

    while q:
        level_length = len(q)
        for i in range(level_length):
            node = q.popleft()
            if i == level_length - 1:
                out.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return out


def test_right_side_view():
    root = build_tree([1,2,3,None,5,None,4])
    rightSideView(root) == [1, 3, 4]
    root = build_tree([])
    rightSideView(root) == []
