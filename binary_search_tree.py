#!/usr/bin/env python
# -*- coding=utf-8 -*-

class TreeNode:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.num_nodes = 0
        self.root = None

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.num_nodes

    def add(self, elem):
        if self.contains(elem):
            return False
        else:
            self.root = self.add_r(self.root, elem)
            self.num_nodes += 1
            return True

    # Recursively add a value in the binary tree
    def add_r(self, node, elem):
        # Base case: we found a leaf node
        if node is None:
            node = TreeNode(elem)
        else:
            if elem < node.data:
                node.left = self.add_r(node.left, elem)
            else:
                node.right = self.add_r(node.right, elem)
        return node

    # Returns True if the element exists in the tree
    def contains(self, elem):
        return self.contains_r(self.root, elem)

    def contains_r(self, node, elem):
        if node is None:
            return False
        
        if elem < node.data:
            return self.contains_r(node.left, elem)
        elif elem > node.data:
            return self.contains_r(node.right, elem)
        else:
            return True

    def inorder_print(self):
        self.inorder_print_r(self.root)
        print('')

    def inorder_print_r(self, node):
        if node:
            self.inorder_print_r(node.left)
            print(node.data, end=' ')
            self.inorder_print_r(node.right)

if __name__ == "__main__":
    bst = BinarySearchTree()
    print('is_empty :', bst.is_empty())
    bst.add(-1)
    bst.add(10)
    bst.add(3)
    bst.add(-1)
    print('inorder_print : ', end= '')
    bst.inorder_print()