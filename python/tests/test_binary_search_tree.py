from src.binary_search_tree import *

def test_add():
    root = None
    root = add(root, 12)
    assert root.data == 12
    root = add(root, 5)
    root = add(root, 18)
    assert root.left.data == 5 and root.right.data == 18


def test_search():
    root = None
    node = search(root, 1)
    assert node is None
    assert not search_iter(root, 1)
    root = add(root, 12)
    root = add(root, 5)
    root = add(root, 18)
    node = search(root, 12)
    assert node.data == 12
    node = search(root, 5)
    assert node.data == 5
    node = search(root, 18)
    assert node.data == 18
    assert not search(root, 10)
    assert search_iter(root, 12)
    assert search_iter(root, 5)
    assert search_iter(root, 18)
    assert not search_iter(root, 10)

    node = search_min(root)
    assert node.data == 5
    node = search_max(root)
    assert node.data == 18


def test_search_successor_predecessor():
    root = None
    data = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
    for d in data:
        root = add(root, d)

    node = search(root, 13)
    assert node.data == 13 and node.parent.data == 7 and node.left.data == 9
    succ = search_successor(node)
    assert succ.data == 15
    node = search(root, 6)
    succ = search_successor(node)
    assert succ.data == 7
    node = search(root, 15)
    succ = search_successor(node)
    assert succ.data == 17

    node = search(root, 9)
    pred = search_predecessor(node)
    assert pred.data == 7
    node = search(root, 6)
    pred = search_predecessor(node)
    assert pred.data == 4
    node = search(root, 17)
    pred = search_predecessor(node)
    assert pred.data == 15
    node = search(root, 15)
    pred = search_predecessor(node)
    assert pred.data == 13
