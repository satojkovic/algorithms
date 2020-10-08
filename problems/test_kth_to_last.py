import unittest
from kth_to_last import *
from nose.tools import eq_

class TestKthToLast(unittest.TestCase):
    def test_kth_to_last(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        kth_node = kth_to_last(head, 2)
        eq_(kth_node.val, 2)
        kth_node = kth_to_last(head, 1)
        eq_(kth_node.val, 3)
        kth_node = kth_to_last(head, 3)
        eq_(kth_node.val, 1)
        kth_node = kth_to_last(head, 10)
        eq_(kth_node, None)

    def test_kth_to_last2(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        kth_node = kth_to_last2(head, 2)
        eq_(kth_node.val, 2)
        kth_node = kth_to_last2(head, 1)
        eq_(kth_node.val, 3)
        kth_node = kth_to_last2(head, 3)
        eq_(kth_node.val, 1)
        kth_node = kth_to_last2(head, 10)
        eq_(kth_node, None)

if __name__ == "__main__":
    unittest.main()
