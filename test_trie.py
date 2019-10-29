import unittest
from trie import *
from nose.tools import eq_

class TestTrie(unittest.TestCase):
    def test_insert_search(self):
        root = TrieNode('')
        root = insert(root, 'a' * 3)
        eq_(root.children['a'].children['a'].children['a'].word_finished, True)
        eq_(root.children['a'].children['a'].word_finished, False)
        root = insert(root, 'a' * 2)
        eq_(root.children['a'].children['a'].word_finished, True)

        eq_(search(root, 'a' * 3), True)
        eq_(search(root, 'a' * 4), False)
        eq_(search(root, 'a' * 2), True)
        eq_(search(root, 'a'), False)

if __name__ == "__main__":
    unittest.main()