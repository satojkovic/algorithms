import unittest
from missing_number import *
from nose.tools import eq_

class TestMissingNumber(unittest.TestCase):
    def test_missing_number1(self):
        eq_(missing_number1([3, 0, 1]), 2)
        eq_(missing_number1([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
        eq_(missing_number1([1, 3, 2]), 0)
        eq_(missing_number1([0]), 1)
        eq_(missing_number1([0, 1]), 2)

    def test_missing_number2(self):
        eq_(missing_number2([3, 0, 1]), 2)
        #eq_(missing_number2([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
        #eq_(missing_number2([1, 3, 2]), 0)
        #eq_(missing_number2([0]), 1)
        #eq_(missing_number2([0, 1]), 2)

    def test_missing_number3(self):
        eq_(missing_number3([3, 0, 1]), 2)

if __name__ == "__main__":
    unittest.main()
