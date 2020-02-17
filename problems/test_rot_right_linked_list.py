import unittest
from rot_right_linked_list import *
from nose.tools import eq_

class TestRotRightLinkedList(unittest.TestCase):
    def test_rot_right_linked_list(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        new_head = rot_right_linked_list(head, 2)
        eq_(new_head.val, 4) # head
        eq_(new_head.next.next.next.next.val, 3) # tail

        head = ListNode(1)
        head.next = ListNode(3)
        head.next.next = ListNode(5)
        new_head = rot_right_linked_list(head, 4)
        eq_(new_head.val, 5) # head
        eq_(new_head.next.next.val, 3) # tail

        head = ListNode(1)
        new_head = rot_right_linked_list(head, 3)
        eq_(new_head.val, 1)
        eq_(new_head.next, None)

if __name__ == "__main__":
    unittest.main()