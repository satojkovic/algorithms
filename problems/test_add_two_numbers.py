import unittest
from add_two_numbers import *
from nose.tools import eq_

class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        l1 = ListNode(2)
        l1.next = ListNode(5)
        l1.next.next = ListNode(5)
        l2 = ListNode(3)
        l2.next = ListNode(5)
        l2.next.next = ListNode(2)
        res = add_two_numbers(l1, l2)
        eq_(res.val, 5)
        eq_(res.next.val, 0)
        eq_(res.next.next.val, 8)
        eq_(res.next.next.next, None)

        l1 = ListNode(9)
        l2 = ListNode(1)
        res = add_two_numbers(l1, l2)
        eq_(res.val, 0)
        eq_(res.next.val, 1)
        eq_(res.next.next, None)

        l1 = ListNode(4)
        l1.next = ListNode(8)
        l2 = ListNode(8)
        l2.next = ListNode(1)
        l2.next.next = ListNode(9)
        res = add_two_numbers(l1, l2)
        eq_(res.val, 2)
        eq_(res.next.val, 0)
        eq_(res.next.next.val, 0)
        eq_(res.next.next.next.val, 1)
        eq_(res.next.next.next.next, None)

if __name__ == "__main__":
    unittest.main()
