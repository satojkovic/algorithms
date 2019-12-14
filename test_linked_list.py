import unittest
from linked_list import LinkedList
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
        eq_(self.l.head.next_elem.data, 1)

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

    def test_remove_nth_from_end(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.head = remove_nth_from_end(ll.head, 2)
        eq_(ll.head.data, 1)
        eq_(ll.head.next_elem.data, 3)
        ll.head = remove_nth_from_end(ll.head, 1)
        eq_(ll.head.data, 1)
        eq_(ll.head.next_elem, None)

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

    def test_get_intersection_node(self):
        l1 = LinkedList()
        l2 = LinkedList()
        node1 = ListElement(3)
        node2 = ListElement(1)
        node3 = ListElement(10)
        node4 = ListElement(9)
        l1.head = node1
        node1.next_elem = node2
        node2.next_elem = node3
        node3.next_elem = node4
        l2.head = node3
        eq_(get_intersection_node(l1.head, l2.head), node3)

        l3 = LinkedList()
        l3.head = ListElement(4)
        eq_(get_intersection_node(l1.head, l3.head), None)

        l4 = LinkedList()
        eq_(get_intersection_node(l1.head, l4.head), None)

    def test_reverse_list(self):
        ll = LinkedList()
        [ll.add(i) for i in range(1, 4)]
        ll.reverse_list()
        eq_(ll.head.data, 3)
        eq_(ll.head.next_elem.data, 2)
        eq_(ll.head.next_elem.next_elem.data, 1)
        eq_(ll.head.next_elem.next_elem.next_elem, None)

        ll = LinkedList()
        ll.add(1)
        ll.reverse_list()
        eq_(ll.head.data, 1)
        eq_(ll.head.next_elem, None)

        ll = LinkedList()
        ll.reverse_list()
        eq_(ll.head, None)

    def test_remove_target_node(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.head = remove_target_node(ll.head, 2)
        eq_(ll.head.data, 1)
        eq_(ll.head.next_elem.data, 3)
        eq_(ll.head.next_elem.next_elem, None)

        ll = LinkedList()
        ll.add(3)
        ll.add(3)
        ll.head = remove_target_node(ll.head, 3)
        eq_(ll.head, None)

        ll = LinkedList()
        ll.add(1)
        ll.head = remove_target_node(ll.head, 10)
        eq_(ll.head.data, 1)
        eq_(ll.head.next_elem, None)

    def test_odd_even_order(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.head = odd_even_order(ll.head)
        eq_(ll.head.data, 1)
        eq_(ll.head.next_elem.data, 3)
        eq_(ll.head.next_elem.next_elem.data, 2)
        eq_(ll.head.next_elem.next_elem.next_elem, None)

        ll = LinkedList()
        ll.add(1)
        ll.head = odd_even_order(ll.head)
        eq_(ll.head.data, 1)
        eq_(ll.head.next_elem, None)

        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.add(4)
        ll.head = odd_even_order(ll.head)
        eq_(ll.head.data, 1)
        eq_(ll.head.next_elem.data, 3)
        eq_(ll.head.next_elem.next_elem.data, 2)
        eq_(ll.head.next_elem.next_elem.next_elem.data, 4)
        eq_(ll.head.next_elem.next_elem.next_elem.next_elem, None)

    def test_is_palindrome(self):
        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.add(2)
        ll.add(1)
        eq_(is_palindrome(ll.head), True)
        eq_(is_palindrome2(ll.head), True)

        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(2)
        ll.add(1)
        eq_(is_palindrome(ll.head), True)
        eq_(is_palindrome2(ll.head), True)

        ll = LinkedList()
        ll.add(1)
        eq_(is_palindrome(ll.head), True)
        eq_(is_palindrome2(ll.head), True)

        ll = LinkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        eq_(is_palindrome(ll.head), False)
        eq_(is_palindrome2(ll.head), False)

        ll = LinkedList()
        eq_(is_palindrome(ll.head), True)
        eq_(is_palindrome2(ll.head), True)


if __name__ == "__main__":
    unittest.main()
