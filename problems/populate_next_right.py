from collections import deque

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

def populate_next_right_v2(root):
    if root is None:
        return root
    q = deque([root])
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i < size - 1:
                node.next = q[0]
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return root

def populate_next_right_v3(root):
    if root is None:
        return root

    leftmost = root
    while leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
            head = head.next
        leftmost = leftmost.left
    return root