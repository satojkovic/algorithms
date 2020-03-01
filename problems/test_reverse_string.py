import unittest
from nose.tools import eq_, ok_
from reverse_string import reverse_string, reverse_string_r

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        s = ['h', 'e', 'l', 'l', 'o']
        eq_(reverse_string(s), ['o', 'l', 'l', 'e', 'h'])

        s = ['H', 'a', 'n', 'n', 'a', 'h']
        eq_(reverse_string(s), ['h', 'a', 'n', 'n', 'a', 'H'])

    def test_reverse_string_r(self):
        s = ['h', 'e', 'l', 'l', 'o']
        eq_(reverse_string_r(s), ['o', 'l', 'l', 'e', 'h'])

        s = ['H', 'a', 'n', 'n', 'a', 'h']
        eq_(reverse_string_r(s), ['h', 'a', 'n', 'n', 'a', 'H'])

if __name__ == "__main__":
    unittest.main()