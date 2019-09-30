import unittest
from doubly_linked_list import DoublyLinkedList, DoublyListElement
from nose.tools import eq_

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dl = DoublyLinkedList()

    def test_is_empty(self):
        eq_(self.dl.is_empty(), True)
        self.dl.insert(DoublyListElement(100))
        eq_(self.dl.is_empty(), False)

    def test_insert(self):
        self.dl.insert(DoublyListElement(10))
        self.dl.insert(DoublyListElement(20))
        self.dl.insert(DoublyListElement(30))
        eq_(self.dl.head.data, 30)
        eq_(self.dl.head.next_elem.data, 20)
        eq_(self.dl.head.next_elem.next_elem.data, 10)

    def test_search(self):
        self.dl.insert(DoublyListElement(10))
        self.dl.insert(DoublyListElement(20))
        self.dl.insert(DoublyListElement(30))
        x = self.dl.search(30)
        eq_(x.prev_elem, None)
        eq_(x.next_elem.data, 20)

        x = self.dl.search(20)
        eq_(x.prev_elem.data, 30)
        eq_(x.next_elem.data, 10)

        x = self.dl.search(10)
        eq_(x.prev_elem.data, 20)
        eq_(x.next_elem, None)

if __name__ == "__main__":
    unittest.main()