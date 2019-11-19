import unittest
from replace_words import *
from nose.tools import eq_

class TetsReplaceWords(unittest.TestCase):
    def test_replace_words(self):
        dict = ['cat', 'bat', 'rat']
        sentence = 'the cattle was rattled by the battery'
        eq_(replace_words(dict, sentence), 'the cat was rat by the bat')

        dict = []
        eq_(replace_words(dict, sentence), sentence)

        dict = ['cat', 'bat', 'rat']
        sentence = ''
        eq_(replace_words(dict, sentence), sentence)

if __name__ == "__main__":
    unittest.main()