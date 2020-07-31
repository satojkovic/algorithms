from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def right_side_view(root):
    if not root:
        return root
    q = deque([(root, 0)])
    nodes = defaultdict(list)
    while q:
        node, level = q.popleft()
        nodes[level].append(node.val)
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
    return [nodes[level][-1] for level in nodes.keys()]
