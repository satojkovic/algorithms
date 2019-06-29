import linked_list
import unittest

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.l = linked_list.LinkedList()

    def test_empty(self):
        self.assertEqual(self.l.is_empty(), True)

    def test_add_first(self):
        self.l.add_first(1)
        self.assertEqual(self.l.size, 1)
        self.assertEqual(self.l.peek_first(), 1)

        self.l.add_first(2)
        self.assertEqual(self.l.size, 2)
        self.assertEqual(self.l.peek_first(), 2)

if __name__ == "__main__":
    unittest.main()
