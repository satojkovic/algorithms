import unittest
from is_happy_number import *
from nose.tools import eq_

class TestIsHappyNumber(unittest.TestCase):
    def test_is_happy_number1(self):
        eq_(is_happy_number1(19), True)
        eq_(is_happy_number1(5), False)
        eq_(is_happy_number1(0), False)

    def test_is_happy_number2(self):
        eq_(is_happy_number2(19), True)
        eq_(is_happy_number2(0), False)

    def test_is_happy_number3(self):
        eq_(is_happy_number3(19), True)
        eq_(is_happy_number3(0), False)

    def test_is_happy_number4(self):
        eq_(is_happy_number4(19), True)
        eq_(is_happy_number4(0), False)

if __name__ == "__main__":
    unittest.main()