import unittest
from max_profit import *
from nose.tools import eq_

class TestMaxProfit(unittest.TestCase):
    def test_max_profit(self):
        eq_(max_profit1([7, 1, 5, 3, 6, 4]), 7)
        eq_(max_profit1([1, 2, 3, 4, 5]), 4)
        eq_(max_profit1([4, 2, 1]), 0)
        eq_(max_profit1([3, 3, 3, 3]), 0)

if __name__ == "__main__":
    unittest.main()
