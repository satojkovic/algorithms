import unittest
from flatten_dbl import *
from nose.tools import eq_

class TestFlattenDbl(unittest.TestCase):
    def test_flatten_dbl(self):
        tail = Node(2, None, None, None)
        child = Node(3, None, None, None)
        head = Node(1, None, tail, child)
        flat = flatten(head)
        eq_(flat.val, 1)
        eq_(flat.next.val, 3)
        eq_(flat.next.next.val, 2)
        eq_(flat.next.next.next, None)

if __name__ == "__main__":
    unittest.main()
