#!/usr/bin/env python
# -*- coding=utf-8 -*-

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    """Inorder traversal
    
    1. Traverse the left subtree
    2. Visit the root node
    3. Traverse the right subtree

    Args:
        root (TreeNode): root node of a tree
    """
    def _inorder(root, visited):
        if root:
            visited = _inorder(root.left, visited)
            visited.append(root.data)
            visited = _inorder(root.right, visited)
        return visited
    visited = []
    return _inorder(root, visited)

def inorder_iter(root):
    s = []
    curr = root
    res = []
    while True:
        if curr is not None:
            s.append(curr)
            curr = curr.left
        elif s:
            node = s.pop()
            res.append(node.data)
            curr = node.right
        else:
            break
    return res

def preorder(root):
    """Preorder traversal

    1. Visit the root node
    2. Traverse the left subtree
    3. Traverse the right subtree
    
    Args:
        root (TreeNode): root node of a tree
    """
    def _preorder(root, visited):
        if root:
            visited.append(root.data)
            visited = _preorder(root.left, visited)
            visited = _preorder(root.right, visited)
        return visited
    visited = []
    return _preorder(root, visited)

def preorder_iter(root):
    stack = [root] if root else []
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited

def postorder(root):
    """Postorder traversal
    
    1. Traverse the left subtree
    2. Traverse the right subtree
    3. Visit the root node

    Args:
        root (TreeNode): root node of a tree
    """
    def _postorder(root, visited):
        if root:
            visited = _postorder(root.left, visited)
            visited = _postorder(root.right, visited)
            visited.append(root.data)
        return visited
    visited = []
    return _postorder(root, visited)

def postorder_iter(root):
    stack = [root] if root else []
    seen, visited = set(), []
    while stack:
        node = stack.pop()
        if (not node.left and not node.right) or node in seen:
            visited.append(node.data)
            continue
        stack.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        seen.add(node)
    return visited

# Level order traversal and output nested lists
def levelorder_r(root):
    res = []
    if root is None:
        return res

    def _levelorder_r(node, level):
        if len(res) == level:
            res.append([])
        res[level].append(node.data)
        if node.left:
            _levelorder_r(node.left, level + 1)
        if node.right:
            _levelorder_r(node.right, level + 1)

    _levelorder_r(root, 0)
    return res

def levelorder(root):
    res = []
    if root is None:
        return res
    q = [root] # deque([root])
    level = 0
    while q:
        res.append([])
        num_nodes_at_level = len(q)
        for _ in range(num_nodes_at_level):
            node = q.pop(0) # q.popleft()
            res[level].append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return res

# Level order traversal and output flattened lists
def levelorder2(root):
    res = []
    if root is None:
        return res
    q = [root]
    while q:
        node = q.pop(0)
        res.append(node.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(10)
    root.left.right = TreeNode(3)
    root.right = TreeNode(20)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)
    print(levelorder_r(root))
    print(levelorder(root))
    print(levelorder2(root))