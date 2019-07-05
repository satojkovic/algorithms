import linked_list
import unittest
from nose.tools import ok_, eq_

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.l = linked_list.LinkedList()

    def test_empty(self):
        ok_(self.l.is_empty())
        self.l.add(1)
        ok_(not self.l.is_empty())

    def test_size(self):
        eq_(self.l.size, 0)
        self.l.add(1)
        eq_(self.l.size, 1)

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

    def test_search(self):
        eq_(self.l.search(linked_list.ListElement(10)), None)
        self.l.add(10)
        eq_(self.l.search(linked_list.ListElement(10)), True)
        eq_(self.l.search(linked_list.ListElement(-1)), False)
        eq_(self.l.search(linked_list.ListElement('a')), False)

    def test_remove_first(self):
        self.l.add(100)
        self.l.add(10)
        eq_(self.l.remove_first(), 100)
        eq_(self.l.remove_first(), 10)

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

if __name__ == "__main__":
    unittest.main()
