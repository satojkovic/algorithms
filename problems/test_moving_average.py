import unittest
from moving_average import *
from nose.tools import eq_

class TestMovingAverage(unittest.TestCase):
    def test_moving_average(self):
        ma = MovingAverage(3)
        eq_(ma.next(1), 1)
        eq_(ma.next(10), (1 + 10) / 2)
        eq_(ma.next(3), (1 + 10 + 3) / 3)
        eq_(ma.next(22), (10 + 3 + 22) / 3)

if __name__ == "__main__":
    unittest.main()