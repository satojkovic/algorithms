from linked_list import SimpleLinkedList


def test_simple_linked_list():
    simple_ll = SimpleLinkedList()
    assert simple_ll.search(10) is None

    [simple_ll.insert(i) for i in range(10, 41, 10)]
    assert simple_ll.head.data == 40

    node = simple_ll.search(20)
    simple_ll.delete(node)
    assert simple_ll.head.next.next.data == 10

    node = simple_ll.search(40)
    simple_ll.delete(node)
    assert simple_ll.head.data == 30

    node = simple_ll.search(100)
    simple_ll.delete(node)
    assert simple_ll.head.data == 30

