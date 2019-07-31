import unittest
from single_number import single_number1, single_number2
from nose.tools import eq_

class TestSingleNumber(unittest.TestCase):
    def test_single_number1(self):
        eq_(single_number1([2, 2, 1]), 1)
        eq_(single_number1([4, 1, 2, 1, 2]), 4)

    def test_single_number2(self):
        eq_(single_number2([2, 2, 1]), 1)
        eq_(single_number2([4, 1, 2, 1, 2]), 4)

if __name__ == "__main__":
    unittest.main()