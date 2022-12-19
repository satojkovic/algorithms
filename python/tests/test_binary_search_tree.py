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
