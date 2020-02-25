class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

def populate_next_right(root):
    if root is None:
        return root
    q = [(root, 0)]
    while q:
        node, level = q.pop(0)
        if q and q[0][1] == level:
            node.next = q[0][0]
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
    return root