import linked_list
import unittest

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.l = linked_list.LinkedList()

    def test_empty(self):
        self.assertEqual(self.l.is_empty(), True)

if __name__ == "__main__":
    unittest.main()
