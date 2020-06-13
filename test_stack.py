import unittest
from stack import Stack
from nose.tools import eq_, ok_
import numpy as np

class TestStack(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_is_empty(self):
        eq_(self.s.is_empty(), True)

    def test_push(self):
        self.s.push(10)
        eq_(self.s.peek(), 10)
        self.s.push(20)
        eq_(self.s.peek(), 20)
        self.s.push('TEST')
        eq_(self.s.peek(), 'TEST')

    def test_pop(self):
        [self.s.push(i) for i in range(5)]
        eq_(self.s.pop(), 4)
        eq_(self.s.pop(), 3)
        eq_(self.s.pop(), 2)
        eq_(self.s.pop(), 1)
        eq_(self.s.pop(), 0)
        eq_(self.s.pop(), None)

    def test_peek(self):
        eq_(self.s.peek(), None)


if __name__ == "__main__":
    unittest.main()