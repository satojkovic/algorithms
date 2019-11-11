import unittest
from recursion import *
from nose.tools import eq_
from linked_list import ListElement
from tree_traversals import TreeNode

class TestRecursion(unittest.TestCase):
    def test_fib(self):
        eq_(fib(0), 0)
        eq_(fib(1), 1)
        eq_(fib(2), 1)
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

    def test_climb_stairs(self):
        eq_(climb_stairs(2), 2)
        eq_(climb_stairs(3), 3)
        eq_(climb_stairs(0), 1)
        eq_(climb_stairs(1), 1)
        eq_(climb_stairs(5), 8)

    def test_pascal_triangle(self):
        eq_(pascal_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
        eq_(pascal_triangle(0), [])
        eq_(pascal_triangle(1), [[1]])
        eq_(pascal_triangle(2), [[1], [1, 1]])

    def test_pascal_triangle2(self):
        eq_(pascal_triangle2(4), [1, 4, 6, 4, 1])
        eq_(pascal_triangle2(0), [1])
        eq_(pascal_triangle2(1), [1, 1])
        eq_(pascal_triangle2(2), [1, 2, 1])

    def test_pascal_triangle3(self):
        eq_(pascal_triangle3(4), [1, 4, 6, 4, 1])
        eq_(pascal_triangle3(0), [1])
        eq_(pascal_triangle3(1), [1, 1])
        eq_(pascal_triangle3(2), [1, 2, 1])

    def test_reverse_list(self):
        head = ListElement(1)
        head.next_elem = ListElement(2)
        head.next_elem.next_elem = ListElement(3)

        rhead = reverse_list(head)
        eq_(rhead.data, 3)
        eq_(rhead.next_elem.data, 2)
        eq_(rhead.next_elem.next_elem.data, 1)
        eq_(rhead.next_elem.next_elem.next_elem, None)

    def test_max_depth(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        eq_(max_depth(root), 2)

        root = TreeNode(10)
        eq_(max_depth(root), 0)

        root = TreeNode(4)
        root.left = TreeNode(1)
        root.right = TreeNode(86)
        eq_(max_depth(root), 1)

    def test_pow(self):
        eq_(pow(2, 10), 1024)
        eq_(pow(2, -2), 0.25)
        eq_(pow(3, 0), 1)
        eq_(pow(0, 0), 1)
        eq_(pow(-4, 3), -64)

    def test_pow2(self):
        eq_(pow2(2, 10), 1024)
        eq_(pow2(2, -2), 0.25)
        eq_(pow2(3, 0), 1)
        eq_(pow2(0, 0), 1)
        eq_(pow2(-4, 3), -64)

    def test_pow3(self):
        eq_(pow3(2, 10), 1024)
        eq_(pow3(2, -2), 0.25)
        eq_(pow3(3, 0), 1)
        eq_(pow3(0, 0), 1)
        eq_(pow3(-4, 3), -64)

    def test_pow4(self):
        eq_(pow4(2, 10), 1024)
        eq_(pow4(2, -2), 0.25)
        eq_(pow4(3, 0), 1)
        eq_(pow4(0, 0), 1)
        eq_(pow4(-4, 3), -64)

    def test_kth_symbol(self):
        eq_(kth_symbol(1, 1), 0)
        eq_(kth_symbol(2, 1), 0)
        eq_(kth_symbol(2, 2), 1)
        eq_(kth_symbol(4, 5), 1)

    def test_kth_symbol2(self):
        eq_(kth_symbol2(1, 1), 0)
        eq_(kth_symbol2(2, 1), 0)
        eq_(kth_symbol2(2, 2), 1)
        eq_(kth_symbol2(4, 5), 1)

    def test_perm(self):
        eq_(perm(3), [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]])
        eq_(perm(0), [])
        eq_(perm(1), [[1]])
        eq_(perm(2), [[2, 1], [1, 2]])

    def test_search_2d_mat(self):
        mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
        eq_(search_2d_mat(mat, 5), True)
        eq_(search_2d_mat(mat, 20), False)

        mat = [[]]
        eq_(search_2d_mat(mat, 20), False)

        mat = [[1, 2, 3]]
        eq_(search_2d_mat(mat, 3), True)
        eq_(search_2d_mat(mat, 10), False)

if __name__ == "__main__":
    unittest.main()