import unittest
from approx_sqrt import *
from nose.tools import eq_

class TestApproxSqrt(unittest.TestCase):
    def test_approx_sqrt(self):
        eq_(approx_sqrt(4), 2)
        eq_(approx_sqrt(15), 3)
        eq_(approx_sqrt(1), 1)

if __name__ == "__main__":
    unittest.main()