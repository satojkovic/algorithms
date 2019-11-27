import unittest
from doubly_linked_list import DoublyLinkedList, DoublyListElement
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
        eq_(dl.head.next_elem.prev_elem.data, 10)
        eq_(dl.head.next_elem.data, 20)
        eq_(dl.head.next_elem.next_elem.prev_elem.data, 20)
        eq_(dl.head.next_elem.next_elem.data, 30)

    def test_is_emtpy_add_at_tail(self):
        dl = DoublyLinkedList()
        eq_(dl.is_empty(), True)
        dl.add_at_tail(10)
        dl.add_at_tail(20)
        dl.add_at_tail(30)
        eq_(dl.is_empty(), False)
        eq_(dl.head.data, 10)
        eq_(dl.head.next_elem.prev_elem.data, 10)
        eq_(dl.head.next_elem.data, 20)
        eq_(dl.head.next_elem.next_elem.prev_elem.data, 20)
        eq_(dl.head.next_elem.next_elem.data, 30)

if __name__ == "__main__":
    unittest.main()