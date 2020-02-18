import unittest
from get_intersect_linked_list import *
from nose.tools import eq_

class TestGetInterSectLinkedList(unittest.TestCase):
    def test_get_intersect_linked_list(self):
        a_0 = ListNode(1)
        a_1 = ListNode(2)
        a_2 = ListNode(3)
        a_0.next = a_1
        a_1.next = a_2

        b_0 = ListNode(11)
        b_1 = a_1
        b_2 = ListNode(33)
        b_0.next = b_1
        b_1.next = b_2

        intersect = get_intersection_node(a_0, b_0)
        eq_(intersect.val, 2)

        c_0 = ListNode(111)
        c_1 = ListNode(222)
        c_0.next = c_1

        intersect = get_intersection_node(a_0, c_0)
        eq_(intersect, None)

if __name__ == "__main__":
    unittest.main()
