import unittest
from doubly_linked_list import DoublyLinkedList, DoublyListNode
from nose.tools import eq_

class TestDoublyLinkedList(unittest.TestCase):
    def test_is_empty_add_at_head(self):
        dl = DoublyLinkedList()
        eq_(dl.is_empty(), True)
        dl.add_at_head(30)
        dl.add_at_head(20)
        dl.add_at_head(10)
        eq_(dl.is_empty(), False)
        eq_(dl.head.data, 10)
        eq_(dl.head.next.prev.data, 10)
        eq_(dl.head.next.data, 20)
        eq_(dl.head.next.next.prev.data, 20)
        eq_(dl.head.next.next.data, 30)

    def test_is_emtpy_add_at_tail(self):
        dl = DoublyLinkedList()
        eq_(dl.is_empty(), True)
        dl.add_at_tail(10)
        dl.add_at_tail(20)
        dl.add_at_tail(30)
        eq_(dl.is_empty(), False)
        eq_(dl.head.data, 10)
        eq_(dl.head.next.prev.data, 10)
        eq_(dl.head.next.data, 20)
        eq_(dl.head.next.next.prev.data, 20)
        eq_(dl.head.next.next.data, 30)

    def test_add_delete_get(self):
        dl = DoublyLinkedList()
        dl.add_at_index(0, 1)
        eq_(dl.get(0), 1)
        eq_(dl.get(1), -1)
        dl.add_at_index(1, 10)
        eq_(dl.get(1), 10)
        dl.add_at_index(1, 100)
        eq_(dl.get(0), 1)
        eq_(dl.get(1), 100)
        eq_(dl.get(2), 10)

        dl.delete_at_index(1)
        eq_(dl.get(0), 1)
        eq_(dl.get(1), 10)
        dl.delete_at_index(0)
        eq_(dl.get(0), 10)
        dl.add_at_index(0, 20)
        dl.delete_at_index(1)
        eq_(dl.get(0), 20)
        dl.delete_at_index(0)
        eq_(dl.get(0), -1)

if __name__ == "__main__":
    unittest.main()