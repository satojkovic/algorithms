from typing import List, Optional
from collections import deque

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


def goodNodes(root: TreeNode) -> int:
    if not root:
        return 0

    s = [(root, root.val)]
    count = 0

    while s:
        node, max_val = s.pop()
        if node.val >= max_val:
            count += 1
            max_val = node.val
        if node.left:
            s.append((node.left, max_val))
        if node.right:
            s.append((node.right, max_val))

    return count


def test_good_nodes():
    root = build_tree([3,1,4,3,None,1,5])
    assert goodNodes(root) == 4

    root = build_tree([3,3,None,4,2])
    assert goodNodes(root) == 3

    root = build_tree([1])
    assert goodNodes(root) == 1
