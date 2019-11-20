import unittest
from circular_queue import *
from nose.tools import eq_

class TestCircularQueue(unittest.TestCase):
    def test_circular_queue(self):
        cq = CircularQueue(3)
        eq_(cq.enqueue(1), True)
        eq_(cq.enqueue(2), True)
        eq_(cq.enqueue(3), True)
        eq_(cq.enqueue(4), False)

        eq_(cq.dequeue(), True)
        eq_(cq.dequeue(), True)
        eq_(cq.dequeue(), True)
        eq_(cq.dequeue(), False)

        cq.enqueue(10)
        eq_(cq.front(), 10)
        eq_(cq.rear(), 10)
        cq.enqueue(20)
        eq_(cq.front(), 10)
        eq_(cq.rear(), 20)

if __name__ == "__main__":
    unittest.main()