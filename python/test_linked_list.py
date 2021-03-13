import unittest
from linked_list import LinkedList
from linked_list import *
from nose.tools import ok_, eq_

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.l = LinkedList()

    def test_empty(self):
        ok_(self.l.is_empty())
        self.l.insert_tail(1)
        ok_(not self.l.is_empty())

    def test_clear(self):
        self.l.insert_tail(1)
        self.l.clear()
        eq_(self.l.head, None)

    def test_size(self):
        eq_(self.l.size, 0)
        self.l.insert_tail(1)
        eq_(self.l.size, 1)

    def test_insert_tail(self):
        self.l.insert_tail(1)
        eq_(self.l.head.data, 1)
        self.l.insert_tail(2)
        eq_(self.l.head.next.data, 2)

    def test_insert_head(self):
        self.l.insert_head(1)
        eq_(self.l.peek_head(), 1)

        self.l.insert_head(2)
        eq_(self.l.peek_head(), 2)
        eq_(self.l.head.next.data, 1)

    def test_remove_head(self):
        self.l.insert_tail(100)
        self.l.insert_tail(10)
        eq_(self.l.remove_head(), 100)
        eq_(self.l.remove_head(), 10)
        eq_(self.l.remove_head(), None)

    def test_remove_last(self):
        self.l.insert_tail(1)
        self.l.insert_tail(2)
        self.l.insert_tail(3)
        eq_(self.l.remove_last(), 3)
        eq_(self.l.remove_last(), 2)
        eq_(self.l.remove_last(), 1)
        eq_(self.l.remove_last(), None)

    def test_remove(self):
        self.l.insert_tail(1)
        self.l.insert_tail(2)
        self.l.insert_tail(3)
        eq_(self.l.remove(2), 2)
        eq_(self.l.head.data, 1)
        eq_(self.l.head.next.data, 3)
        eq_(self.l.remove(3), 3)
        eq_(self.l.head.data, 1)
        eq_(self.l.head.next, None)

    def test_search(self):
        eq_(self.l.search(10), False)
        self.l.insert_tail(10)
        self.l.insert_head(-1)
        eq_(self.l.search(10), True)
        eq_(self.l.search(-1), True)
        eq_(self.l.search('a'), False)

    def test_find_middle(self):
        self.l.insert_tail(1)
        self.l.insert_tail(2)
        self.l.insert_tail(3)
        self.l.insert_tail(4)
        self.l.insert_tail(5)
        # odd case
        eq_(self.l.find_middle(), 3)

        # even case: 1->2->3->4
        self.l.remove_last()
        eq_(self.l.find_middle(), 2)

        # 1
        [self.l.remove_last() for _ in range(3)]
        eq_(self.l.find_middle(), 1)

        # empty
        self.l.remove_head()
        eq_(self.l.find_middle(), None)

    def test_remove_nth_from_end(self):
        ll = LinkedList()
        ll.insert_tail(1)
        ll.insert_tail(2)
        ll.insert_tail(3)
        ll.head = remove_nth_from_end(ll.head, 2)
        eq_(ll.head.data, 1)
        eq_(ll.head.next.data, 3)
        ll.head = remove_nth_from_end(ll.head, 1)
        eq_(ll.head.data, 1)
        eq_(ll.head.next, None)

    def test_detect_loop(self):
        ll = LinkedList()
        node1 = ListElement(3)
        node2 = ListElement(1)
        node3 = ListElement(10)
        ll.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node2
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
        node1.next = node2
        node2.next = node3
        node3.next = node2
        eq_(ll.detect_loop_start(), node2)

        ll.clear()
        ll.head = ListElement(100)
        eq_(ll.detect_loop_start(), None)

    def test_reverse_list(self):
        ll = LinkedList()
        [ll.insert_tail(i) for i in range(1, 4)]
        reversed = ll.reverse_list()
        eq_(reversed.data, 3)
        eq_(reversed.next.data, 2)
        eq_(reversed.next.next.data, 1)
        eq_(reversed.next.next.next, None)

        ll = LinkedList()
        ll.insert_tail(1)
        reversed = ll.reverse_list()
        eq_(reversed.data, 1)
        eq_(reversed.next, None)

        ll = LinkedList()
        reversed = ll.reverse_list()
        eq_(reversed, None)

    def test_remove_target_node(self):
        ll = LinkedList()
        ll.insert_tail(1)
        ll.insert_tail(2)
        ll.insert_tail(3)
        ll.head = remove_target_node(ll.head, 2)
        eq_(ll.head.data, 1)
        eq_(ll.head.next.data, 3)
        eq_(ll.head.next.next, None)

        ll = LinkedList()
        ll.insert_tail(3)
        ll.insert_tail(3)
        ll.head = remove_target_node(ll.head, 3)
        eq_(ll.head, None)

        ll = LinkedList()
        ll.insert_tail(1)
        ll.head = remove_target_node(ll.head, 10)
        eq_(ll.head.data, 1)
        eq_(ll.head.next, None)

    def test_odd_even_order(self):
        ll = LinkedList()
        ll.insert_tail(1)
        ll.insert_tail(2)
        ll.insert_tail(3)
        ll.head = odd_even_order(ll.head)
        eq_(ll.head.data, 1)
        eq_(ll.head.next.data, 3)
        eq_(ll.head.next.next.data, 2)
        eq_(ll.head.next.next.next, None)

        ll = LinkedList()
        ll.insert_tail(1)
        ll.head = odd_even_order(ll.head)
        eq_(ll.head.data, 1)
        eq_(ll.head.next, None)

        ll = LinkedList()
        ll.insert_tail(1)
        ll.insert_tail(2)
        ll.insert_tail(3)
        ll.insert_tail(4)
        ll.head = odd_even_order(ll.head)
        eq_(ll.head.data, 1)
        eq_(ll.head.next.data, 3)
        eq_(ll.head.next.next.data, 2)
        eq_(ll.head.next.next.next.data, 4)
        eq_(ll.head.next.next.next.next, None)

    def test_rotate(self):
        ll = LinkedList()
        ll.insert_tail(1)
        ll.insert_tail(2)
        ll.insert_tail(3)
        ll.insert_tail(4)
        ll.insert_tail(5)
        ll.rotate(2)
        eq_(ll.head.data, 4)

        ll = LinkedList()
        ll.insert_tail(1)
        ll.rotate(3)
        eq_(ll.head.data, 1)

if __name__ == "__main__":
    unittest.main()
