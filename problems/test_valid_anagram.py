import unittest
from valid_anagram import *
from nose.tools import eq_

class TestValidAnagram(unittest.TestCase):
    def test_valid_anagram1(self):
        eq_(valid_anagram1('anagram', 'nagaram'), True)
        eq_(valid_anagram1('rat', 'car'), False)
        eq_(valid_anagram1('', 'abc'), False)
        eq_(valid_anagram1('abc', ''), False)
        eq_(valid_anagram1('', ''), True)

if __name__ == "__main__":
    unittest.main()