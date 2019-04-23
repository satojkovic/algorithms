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

    def remove(self, elem):
        if self.contains(elem):
            self.root = self.remove_r(self.root, elem)
            self.num_nodes -= 1
            return True
        else:
            return False

    def remove_r(self, node, elem):
        if node is None:
            return None

        # Dig into left subtree, the value we're looking for is
        # samller than the current value
        if node.data > elem:
            node.left = self.remove_r(node.left, elem)
        # Dig into right subtree, the value we're looking for is
        # larger than the current value
        elif node.data < elem:
            node.right = self.remove_r(node.right, elem)
        # Found the node we wish to remove
        else:
            # In this situation just swap the node we wish to remove
            # with its right child
            if node.left is None:
                return node.right
            # In this situation just swap the node we wish to remove
            # with its left child
            elif node.right is None:
                return node.left
            # when removing a node from a binary tree with two links
            # the successor of the node being removed can either be the
            # largest value in the left subtree or the smallest value in the right subtree.
            # In this implementation, I have decided to find the smallest value in the right subtree
            # which can be found by traversing as far as possible in the right subtree.
            else:
                # Find the leftmost node in the right subtree
                tmp = self.dig_left(node.right)

                # swap the data
                node.data = tmp

                # Go into the right subtree and remove the leftmost
                # node we found and swapped data with.
                # This prevents us from having two nodes in our tree with the same value
                node.right = remove(node.right, tmp.data)

        return node

    def dig_left(self, node):
        cur = node
        while cur.left:
            cur = cur.left
        return cur

    def inorder_print(self):
        self.inorder_print_r(self.root)
        print('')

    def inorder_print_r(self, node):
        if node:
            self.inorder_print_r(node.left)
            print(node.data, end=' ')
            self.inorder_print_r(node.right)

    def levelorder_print(self):
        q = [self.root]
        while q:
            node = q.pop(0)
            print(node.data, end=' ')
            q = q + [node.left] if node.left else q
            q = q + [node.right] if node.right else q
        print('')

if __name__ == "__main__":
    bst = BinarySearchTree()
    print('is_empty :', bst.is_empty())
    bst.add(3)
    bst.add(2)
    bst.add(5)
    bst.add(-1)
    bst.add(0)
    bst.add(10)
    bst.add(0)
    print('inorder_print : ', end= '')
    bst.inorder_print()
    print('levelorder_print : ', end='')
    bst.levelorder_print()