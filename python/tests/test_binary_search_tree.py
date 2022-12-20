import pytest
from src.binary_search_tree import *

@pytest.fixture
def empty_bst():
    root = None
    return root


@pytest.fixture
def simple_bst():
    root = None
    data = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
    for d in data:
        root = add(root, d)
    return root


def test_add(empty_bst):
    root = add(empty_bst, 12)
    assert root.data == 12
    root = add(root, 5)
    root = add(root, 18)
    assert root.left.data == 5 and root.right.data == 18


def test_add_iter(empty_bst, simple_bst):
    root = add_iter(empty_bst, TreeNode(15))
    assert root.data == 15 and root.left is None and root.right is None and root.parent is None
    root = add_iter(root, TreeNode(6))
    assert root.left.data == 6 and root.left.parent.data == 15
    root = add_iter(root, TreeNode(18))
    assert root.right.data == 18 and root.right.parent.data == 15
    root = add_iter(root, TreeNode(3))
    assert root.left.left.data == 3 and root.left.left.parent.data == 6
    root = add_iter(root, TreeNode(20))
    assert root.right.right.data == 20 and root.right.right.parent.data == 18


def test_search(simple_bst):
    assert search(simple_bst, 1) is None
    assert search_iter(simple_bst, 1) is None

    node = search(simple_bst, 18)
    assert node.data == 18
    node = search_iter(simple_bst, 18)
    assert node.data == 18

    node = search_min(simple_bst)
    assert node.data == 2
    node = search_max(simple_bst)
    assert node.data == 20


def test_search_successor_predecessor(simple_bst):
    node = search(simple_bst, 13)
    succ = search_successor(node)
    assert succ.data == 15
    
    node = search(simple_bst, 6)
    succ = search_successor(node)
    assert succ.data == 7

    node = search(simple_bst, 15)
    succ = search_successor(node)
    assert succ.data == 17

    node = search(simple_bst, 9)
    pred = search_predecessor(node)
    assert pred.data == 7
    
    node = search(simple_bst, 6)
    pred = search_predecessor(node)
    assert pred.data == 4
    
    node = search(simple_bst, 17)
    pred = search_predecessor(node)
    assert pred.data == 15
    
    node = search(simple_bst, 15)
    pred = search_predecessor(node)
    assert pred.data == 13
