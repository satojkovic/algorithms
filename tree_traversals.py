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

    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def inorder_retlist(root):
    def helper(root, path):
        if root is None:
            return path
        path = helper(root.left, path)
        path.append(root.data)
        path = helper(root.right, path)
        return path

    path = []
    path = helper(root, path)
    return path

def inorder_retlist2(root):
    if root is None:
        return []

    left = inorder_retlist2(root.left)
    right = inorder_retlist2(root.right)
    return left + [root.data] + right

def preorder(root):
    """Preorder traversal

    1. Visit the root node
    2. Traverse the left subtree
    3. Traverse the right subtree
    
    Args:
        root (TreeNode): root node of a tree
    """

    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    """Postorder traversal
    
    1. Traverse the left subtree
    2. Traverse the right subtree
    3. Visit the root node

    Args:
        root (TreeNode): root node of a tree
    """

    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print('Inorder:', end=' ')
    inorder(root)
    print()
    print('Preorder:', end=' ')
    preorder(root)
    print()
    print('Postorder:', end=' ')
    postorder(root)
    print()