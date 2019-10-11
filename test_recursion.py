import unittest
from recursion import *
from nose.tools import eq_
from linked_list import ListElement

class TestRecursion(unittest.TestCase):
    def test_fib(self):
        eq_(fib(0), 0)
        eq_(fib(1), 1)
        eq_(fib(10), 55)

    def tets_fib_memo(self):
        eq_(fib_memo(0), 0)
        eq_(fib_memo(1), 1)
        eq_(fib_memo(2), 1)
        eq_(fib_memo(10), 55)

    def test_reverse_str(self):
        eq_(reverse_str('abcde'), 'edcba')
        eq_(reverse_str('A'), 'A')
        eq_(reverse_str(''), '')
        eq_(reverse_str('AB'), 'BA')

    def test_reverse_str2(self):
        eq_(reverse_str2(['a', 'b', 'c', 'd', 'e']), ['e', 'd', 'c', 'b', 'a'])
        eq_(reverse_str2(['A']), ['A'])
        eq_(reverse_str2([]), [])
        eq_(reverse_str2(['A', 'B']), ['B', 'A'])

    def test_reverse_str3(self):
        s = ['a', 'b', 'c', 'd', 'e']
        reverse_str3(s, 0, len(s) - 1)
        eq_(s, ['e', 'd', 'c', 'b', 'a'])

        s = ['A']
        reverse_str3(s, 0, len(s) - 1)
        eq_(s, ['A'])

        s = []
        reverse_str3(s, 0, len(s) - 1)
        eq_(s, [])

        s = ['A', 'B']
        reverse_str3(s, 0, len(s) - 1)
        eq_(s, ['B', 'A'])

    def test_swap_node_pairs(self):
        head = ListElement(1)
        head.next_elem = ListElement(2)
        head.next_elem.next_elem = ListElement(3)
        head.next_elem.next_elem.next_elem = ListElement(4)

        swap_head = swap_node_pairs(head)
        eq_(swap_head.data, 2)
        eq_(swap_head.next_elem.data, 1)
        eq_(swap_head.next_elem.next_elem.data, 4)
        eq_(swap_head.next_elem.next_elem.next_elem.data, 3)
        eq_(swap_head.next_elem.next_elem.next_elem.next_elem, None)

if __name__ == "__main__":
    unittest.main()