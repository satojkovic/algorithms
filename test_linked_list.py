import unittest
from linked_list import *
from nose.tools import ok_, eq_

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.l = LinkedList()

    def test_empty(self):
        ok_(self.l.is_empty())
        self.l.add(1)
        ok_(not self.l.is_empty())

    def test_clear(self):
        self.l.add(1)
        self.l.clear()
        eq_(self.l.head, None)

    def test_size(self):
        eq_(self.l.size, 0)
        self.l.add(1)
        eq_(self.l.size, 1)

    def test_add(self):
        self.l.add(1)
        eq_(self.l.head.data, 1)
        self.l.add(2)
        eq_(self.l.head.next_elem.data, 2)

    def test_add_first(self):
        self.l.add_first(1)
        eq_(self.l.peek_first(), 1)

        self.l.add_first(2)
        eq_(self.l.peek_first(), 2)

    def test_add_last(self):
        self.l.add_last(3)
        eq_(self.l.peek_last(), 3)
        self.l.add_last(4)
        eq_(self.l.peek_last(), 4)

    def test_remove_first(self):
        self.l.add(100)
        self.l.add(10)
        eq_(self.l.remove_first(), 100)
        eq_(self.l.remove_first(), 10)
        eq_(self.l.remove_first(), None)

    def test_remove_last(self):
        self.l.add(1)
        self.l.add(2)
        self.l.add(3)
        eq_(self.l.remove_last(), 3)
        eq_(self.l.remove_last(), 2)
        eq_(self.l.remove_last(), 1)
        eq_(self.l.remove_last(), None)

    def test_remove(self):
        self.l.add(1)
        self.l.add(2)
        self.l.add(3)
        eq_(self.l.remove(self.l.head.next_elem), True)
        eq_(self.l.head.data, 1)
        eq_(self.l.head.next_elem.data, 3)

    def test_search(self):
        eq_(self.l.search(ListElement(10)), None)
        self.l.add(10)
        eq_(self.l.search(ListElement(10)), True)
        eq_(self.l.search(ListElement(-1)), False)
        eq_(self.l.search(ListElement('a')), False)

    def test_find_middle(self):
        self.l.add(1)
        self.l.add(2)
        self.l.add(3)
        self.l.add(4)
        self.l.add(5)
        # odd case
        eq_(self.l.find_middle(), 3)

        # even case: 1->2->3->4
        self.l.remove_last()
        eq_(self.l.find_middle(), 2)

        # 1
        [self.l.remove_last() for _ in range(3)]
        eq_(self.l.find_middle(), 1)

        # empty
        self.l.remove_first()
        eq_(self.l.find_middle(), None)

    def test_find_nth_from_end(self):
        # 0->1->2->3->4
        [self.l.add(i) for i in range(5)]
        ret = self.l.find_nth_from_end(1)
        eq_(ret.data, 4)
        ret = self.l.find_nth_from_end(2)
        eq_(ret.data, 3)
        ret = self.l.find_nth_from_end(3)
        eq_(ret.data, 2)
        ret = self.l.find_nth_from_end(4)
        eq_(ret.data, 1)
        ret = self.l.find_nth_from_end(5)
        eq_(ret.data, 0)

        eq_(self.l.find_nth_from_end(0), None)
        eq_(self.l.find_nth_from_end(6), None)
        eq_(self.l.find_nth_from_end(-1), None)

    def test_detect_loop(self):
        ll = LinkedList()
        node1 = ListElement(3)
        node2 = ListElement(1)
        node3 = ListElement(10)
        ll.head = node1
        node1.next_elem = node2
        node2.next_elem = node3
        node3.next_elem = node2
        eq_(ll.detect_loop(), True)

        ll.clear()
        ll.head = ListElement(100)
        eq_(ll.detect_loop(), False)

    def test_detect_loop_start(self):
        ll = LinkedList()
        node1 = ListElement(3)
        node2 = ListElement(1)
        node3 = ListElement(10)
        ll.head = node1
        node1.next_elem = node2
        node2.next_elem = node3
        node3.next_elem = node2
        eq_(ll.detect_loop_start(), node2)

        ll.clear()
        ll.head = ListElement(100)
        eq_(ll.detect_loop_start(), None)

if __name__ == "__main__":
    unittest.main()
