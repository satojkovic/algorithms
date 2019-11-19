import unittest
from queue import *
from nose.tools import eq_

class TestQueue(unittest.TestCase):
    def test_enque(self):
        q = Queue()
        [q.enque(i) for i in [5, 13, 8, 2, 10]]
        eq_(q.head.data, 5)
        eq_(q.tail.data, 10)

    def test_deque(self):
        q = Queue()
        [q.enque(i) for i in [5, 13, 8]]
        eq_(q.deque(), 5)
        eq_(q.deque(), 13)
        eq_(q.deque(), 8)
        eq_(q.deque(), None)

if __name__ == "__main__":
    unittest.main()