#!/usr/bin/env python
# -*- coding=utf-8 -*-

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


def inorder_print(root):
    if root:
        inorder_print(root.left)
        print(root.data, end=' ')
        inorder_print(root.right)


def add(root, data):
    if root is None:
        return TreeNode(data)

    if data < root.data:
        left = add(root.left, data)
        root.left = left
        left.parent = root
    else:
        right = add(root.right, data)
        root.right = right
        right.parent = root
    return root


def test_add():
    root = None
    root = add(root, 12)
    assert root.data == 12
    root = add(root, 5)
    root = add(root, 18)
    assert root.left.data == 5 and root.right.data == 18


def search(root, data):
    if root is None:
        return False

    if root.data == data:
        return True
    elif data < root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)


def test_search():
    root = None
    assert not search(root, 1)
    root = add(root, 12)
    root = add(root, 5)
    root = add(root, 18)
    assert search(root, 12)
    assert search(root, 5)
    assert search(root, 18)
    assert not search(root, 10)


def search_iter(root, elem):
    while root is not None and root.data != elem:
        root = root.left if elem < root.data else root.right
    return root

def remove(root, elem):
    if not root:
        return None

    if elem < root.data:
        root.left = remove(root.left, elem)
    elif root.data < elem:
        root.right = remove(root.right, elem)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            # Find the rightmost node in the left subtree
            tmp = dig_right(root.left)
            root.data = tmp.data
            root.left = remove(root.left, tmp.data)
    return root

def dig_right(node):
    cur = node
    while cur.right:
        cur = cur.right
    return cur


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
        self.root = self._add(self.root, elem)
        self.num_nodes += 1
        return True

    # Recursively add a value in the binary tree
    def _add(self, node, elem):
        # Base case: we found a leaf node (the place where inserting an elem)
        if node is None:
            return TreeNode(elem)
        # Already checked the same value by contains() method
        if elem < node.data:
            node.left = self._add(node.left, elem)
        else:
            node.right = self._add(node.right, elem)
        return node

    # Return the node if the element exists in the tree
    def search(self, elem):
        return self._search(self.root, elem)

    def _search(self, node, elem):
        if node is None or elem == node.data:
            return node
        if elem < node.data:
            return self._search(node.left, elem)
        return self._search(node.right, elem)

    # Returns True if the element exists in the tree
    def contains(self, elem):
        return self._contains(self.root, elem)

    def _contains(self, node, elem):
        if node is None:
            return False
        
        if elem < node.data:
            return self._contains(node.left, elem)
        elif elem > node.data:
            return self._contains(node.right, elem)
        else:
            return True

    def remove(self, elem):
        if self.contains(elem):
            self.root = self._remove(self.root, elem)
            self.num_nodes -= 1
            return True
        else:
            return False

    def _remove(self, node, elem):
        if node is None:
            return None

        # Dig into left subtree, the value we're looking for is
        # samller than the current value
        if node.data > elem:
            node.left = self._remove(node.left, elem)
        # Dig into right subtree, the value we're looking for is
        # larger than the current value
        elif node.data < elem:
            node.right = self._remove(node.right, elem)
        # Found the node we wish to remove
        else:
            # In this situation just swap the node we wish to remove
            # with its right child
            # if right child is also None, return None(i.e. remove leaf node)
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
                node.data = tmp.data

                # Go into the right subtree and remove the leftmost
                # node we found and swapped data with.
                # This prevents us from having two nodes in our tree with the same value
                node.right = self._remove(node.right, tmp.data)

        return node

    def dig_left(self, node):
        cur = node
        while cur.left:
            cur = cur.left
        return cur

    def inorder_print(self):
        self._inorder_print(self.root)
        print('')

    def _inorder_print(self, node):
        if node:
            self._inorder_print(node.left)
            print(node.data, end=' ')
            self._inorder_print(node.right)

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
    bst.add(10)
    bst.add(4)
    bst.add(1)
    bst.add(5)
    bst.add(6)
    bst.add(20)
    bst.add(15)
    bst.add(33)
    bst.add(19)
    bst.add(30)
    bst.add(49)
    print('inorder_print:')
    bst.inorder_print()
    print('levelorder_print:')
    bst.levelorder_print()

    target = 10
    if bst.search(target):
        print('Search {} -> Found'.format(target))
    else:
        print('Search {} -> Not found'.format(target))

    target = -100
    if bst.search(target):
        print('Search {} -> Found'.format(target))
    else:
        print('Search {} -> Not found'.format(target))

    print('remove(1):')
    if bst.remove(1):
        bst.levelorder_print()
    else:
        print('remove failed.')
    print('remove(20):')
    if bst.remove(20):
        bst.levelorder_print()
    else:
        print('remove failed.')

    root = None
    root = add(root, 10)
    inorder_print(root)
    print()
    root = add(root, 4)
    inorder_print(root)
    print()
    root = add(root, 5)
    inorder_print(root)
    print()
    root = add(root, 1)
    inorder_print(root)
    print()
    root = add(root, 6)
    inorder_print(root)
    print()
    root = add(root, 20)
    inorder_print(root)
    print()
    root = add(root, 15)
    inorder_print(root)
    print()
    root = add(root, 33)
    inorder_print(root)
    print()
    root = add(root, 49)
    inorder_print(root)
    print()
    root = add(root, 30)
    inorder_print(root)
    print()

    target = -1
    node = search(root, target)
    if node:
        print('Found: {}'.format(node.data))
    else:
        print('Not found(search {})'.format(target))

    root = remove(root, 20)
    if root:
        inorder_print(root)
        print()
    else:
        print('remove failed.')
