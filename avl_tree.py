#!/usr/bin/env python
# -*- coding=utf-8 -*-

class AVLTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0
        self.bf = 0 # balanced factor = height(node.right) - height(node.left)

class AVLTree:
    def __init__(self):
        self.root = None
        self.node_count = 0

    def height(self):
        if not self.root:
            return 0
        return self.root.height

    def insert(self, value):
        if not value:
            return False
        if not self._contains(self.root, value):
            self.root = self._insert(self.root, value)
            self.node_count += 1
            return True
        return False

    def _contains(self, node, value):
        if not node:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._contains(node.left, value)
        else:
            return self._contains(node.right, value)

    def _insert(self, node, value):
        if not node:
            return AVLTreeNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        # Update balance factor and height values
        self._update(node)

        # Re-balance tree
        return self._balance(node)

    def _update(self, node):
        lh = -1
        rh = -1
        if node.left:
            lh = node.left.height
        if node.right:
            rh = node.right.height
        # Assign 0 when there are no child nodes
        node.height = 1 + max(lh, rh)

        # Update balance factor
        node.bf = rh - lh

    def _balance(self, node):
        # left heavy subtree
        if node.bf == -2:
            if node.left.bf <= 0:
                return self._left_left_case(node)
            else:
                return self._left_right_case(node)
        elif node.bf == 2:
            if node.right.bf <= 0:
                return self._right_left_case(node)
            else:
                return self._right_right_case(node)
        return node

    def _left_left_case(self, node):
        return self._right_rot(node)

    def _left_right_case(self, node):
        node.left = self._left_rot(node.left)
        return self._left_left_case(node)

    def _right_left_case(self, node):
        node.right = self._right_rot(node.right)
        return self._right_right_case(node)

    def _right_right_case(self, node):
        return self._left_rot(node)

    def _right_rot(self, node):
        b = node.left
        node.left = b.right
        b.right = node
        # After rotation update bf and height
        self._update(node)
        self._update(b)
        return b

    def _left_rot(self, node):
        b = node.right
        node.right = b.left
        b.left = node
        # After rotation update bf and height
        self._update(node)
        self._update(b)
        return b