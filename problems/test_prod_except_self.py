import unittest
from prod_except_self import *
from nose.tools import eq_

class TestProdExceptSelf(unittest.TestCase):
    def test_prod_except_self(self):
        eq_(prod_except_self1([1, 2, 3, 4]), [24, 12, 8, 6])
        eq_(prod_except_self1([10, 20]), [20, 10])
        eq_(prod_except_self1([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()