import unittest
from merge_two_sorted_list import *
from nose.tools import eq_

class TestMergeTwoSortedList(unittest.TestCase):
    def setUp(self):
        self.l1 = ListNode(1)
        self.l1.next = ListNode(2)
        self.l1.next.next = ListNode(4)
        self.l1.next.next.next = ListNode(5)

        self.l2 = ListNode(1)
        self.l2.next = ListNode(3)
        self.l2.next.next = ListNode(4)

        self.l2_2 = ListNode(123)

    def test_merge_two_sorted_list1(self):
        head = merge_two_sorted_list1(self.l1, self.l2)
        ret = []
        while head:
            ret.append(head.val)
            head = head.next
        eq_(ret, [1, 1, 2, 3, 4, 4, 5])

        head = merge_two_sorted_list1(self.l1, None)
        ret = []
        while head:
            ret.append(head.val)
            head = head.next
        eq_(ret, [1, 2, 4, 5])

        head = merge_two_sorted_list1(None, self.l2)
        ret = []
        while head:
            ret.append(head.val)
            head = head.next
        eq_(ret, [1, 3, 4])

        head = merge_two_sorted_list1(None, None)
        ret = []
        while head:
            ret.append(head.val)
            head = head.next
        eq_(ret, [])

        head = merge_two_sorted_list1(self.l1, self.l2_2)
        ret = []
        while head:
            ret.append(head.val)
            head = head.next
        eq_(ret, [1, 2, 4, 5, 123])

if __name__ == "__main__":
    unittest.main()