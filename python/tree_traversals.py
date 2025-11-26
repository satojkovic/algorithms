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
    stack = []
    curr = root
    res = []
    # Repeat until the current node is None and stack is also empty
    while stack or curr != None:
        # Push the current node to the stack and set the left as the current
        if curr != None:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            res.append(curr.data)
            curr = curr.right
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
    from collections import deque
    stack = [root] if root else []
    visited = deque()
    while stack:
        node = stack.pop()
        visited.appendleft(node.data)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return list(visited)


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
    from collections import deque
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        num_nodes_at_level = len(q)
        current_level_nodes = []
        for _ in range(num_nodes_at_level):
            node = q.popleft()
            current_level_nodes.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(current_level_nodes)
    return result


def test_tree_traversals():
    root = TreeNode(1)
    root.left = TreeNode(10)
    root.left.right = TreeNode(3)
    root.right = TreeNode(20)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)

    assert inorder(root) == [10, 3, 1, 9, 20, 11]
    assert inorder_iter(root) == [10, 3, 1, 9, 20, 11]
    assert preorder(root) == [1, 10, 3, 20, 9, 11]
    assert preorder_iter(root) == [1, 10, 3, 20, 9, 11]
    assert postorder(root) == [3, 10, 9, 11, 20, 1]

    assert levelorder(root) == [[1], [10, 20], [3, 9, 11]]
    assert levelorder_r(root) == [[1], [10, 20], [3, 9, 11]]

