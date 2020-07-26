import unittest
from min_move import *
from nose.tools import eq_

class TestMinMove(unittest.TestCase):
    def test_min_move(self):
        eq_(min_move([24, 19, 100, 52, 3]), 130)
        eq_(min_move([10, 20, 100, 50]), 120)
        eq_(min_move([1]), 0)
        eq_(min_move([10, 10, 10]), 0)

if __name__ == "__main__":
    unittest.main()