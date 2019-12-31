import unittest
from single_number import *
from nose.tools import eq_

class TestSingleNumber(unittest.TestCase):
    def test_single_number1(self):
        eq_(single_number1([2, 2, 1]), 1)
        eq_(single_number1([4, 1, 2, 1, 2]), 4)
        eq_(single_number1([1]), 1)

    def test_single_number2(self):
        eq_(single_number2([2, 2, 1]), 1)
        eq_(single_number2([4, 1, 2, 1, 2]), 4)
        eq_(single_number2([1]), 1)

    def test_single_number3(self):
        eq_(single_number3([2, 2, 1]), 1)
        eq_(single_number3([4, 1, 2, 1, 2]), 4)
        eq_(single_number3([1]), 1)

if __name__ == "__main__":
    unittest.main()