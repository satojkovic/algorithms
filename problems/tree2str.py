from tkinter.tix import Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree2str(root):
    left, right = '', ''
    if root.left:
        left = ''.join(['(', tree2str(root.left), ')'])
    else:
        left = '()' if root.right else ''
    if root.right:
        right = ''.join(['(', tree2str(root.right), ')'])
    return ''.join([str(root.val), left, right])


def test_tree2str():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    assert tree2str(root) == '1(2(4))(3)'

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    assert tree2str(root) == '1(2()(4))(3)'
