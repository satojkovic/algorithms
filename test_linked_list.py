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

if __name__ == "__main__":
    unittest.main()
