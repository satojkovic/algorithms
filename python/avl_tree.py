#!/usr/bin/env python
# -*- coding=utf-8 -*-

class AVLTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0
        # balanced factor = height(node.right) - height(node.left)
        # height(x) is calculated as the number of edges between x and furthest leaf
        self.bf = 0

class AVLTree:
    def __init__(self):
        self.root = None
        self.node_count = 0

    def height(self):
        if not self.root:
            return 0
        return self.root.height

    def insert(self, value):
        if value is None:
            return False

        # Only insert unique values
        if not self._contains(self.root, value):
            self.root = self._insert(self.root, value)
            self.node_count += 1
            return True

        # Value already exists in the tree
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
        lh = node.left.height if node.left else -1
        rh = node.right.height if node.right else -1
        # Assign 0 when there are no child nodes
        node.height = 1 + max(lh, rh)

        # Update balance factor
        node.bf = rh - lh

    def _balance(self, node):
        # Left heavy subtree
        if node.bf == -2:
            if node.left.bf <= 0:
                #     3
                #    /
                #   2
                #  /
                # 1
                # We need right rotation
                return self._left_left_case(node)
            else:
                #   3
                #  /
                # 1
                #  \
                #   2
                # We need left and right rotation(after left rotation, equal to the left_left_case)
                return self._left_right_case(node)
        # Right heavy subtree
        elif node.bf == 2:
            if node.right.bf <= 0:
                # 1
                #  \
                #   3
                #  /
                # 2
                # We need right and left rotation(after right rotation, equal to the right_right_case)
                return self._right_left_case(node)
            else:
                # 1
                #  \
                #   2
                #    \
                #     3
                # We need left rotation
                return self._right_right_case(node)
        # Node has balance factor of -1 or 0 or 1
        # Therefore we don't need to balance
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