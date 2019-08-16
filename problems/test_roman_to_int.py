import unittest
from roman_to_int import *
from nose.tools import eq_

class TestRomanToInt(unittest.TestCase):
    def test_roman_to_int1(self):
        eq_(roman_to_int1('III'), 3)
        eq_(roman_to_int1('IX'), 9)
        eq_(roman_to_int1('XII'), 12)
        eq_(roman_to_int1('XL'), 40)
        eq_(roman_to_int1('CM'), 900)
        eq_(roman_to_int1('MCMXCIV'), 1994)
        eq_(roman_to_int1('I'), 1)

    def test_roman_to_int2(self):
        eq_(roman_to_int2('III'), 3)
        eq_(roman_to_int2('IX'), 9)
        eq_(roman_to_int2('XII'), 12)
        eq_(roman_to_int2('XL'), 40)
        eq_(roman_to_int2('CM'), 900)
        eq_(roman_to_int2('MCMXCIV'), 1994)
        eq_(roman_to_int2('I'), 1)

    def test_roman_to_int3(self):
        eq_(roman_to_int3('III'), 3)
        eq_(roman_to_int3('IX'), 9)
        eq_(roman_to_int3('XII'), 12)
        eq_(roman_to_int3('XL'), 40)
        eq_(roman_to_int3('CM'), 900)
        eq_(roman_to_int3('MCMXCIV'), 1994)
        eq_(roman_to_int3('I'), 1)

if __name__ == "__main__":
    unittest.main()