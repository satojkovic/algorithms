import unittest
from trie import *
from nose.tools import eq_

class TestTrie(unittest.TestCase):
    def test_insert(self):
        root = TrieNode('')
        root.children['a'] = TrieNode('a')
        root.children['a'].children['m'] = TrieNode('am')
        root.children['b'] = TrieNode('b')
        root.children['b'].children['e'] = TrieNode('be')
        root.children['b'].children['a'] = TrieNode('ba')
        root.children['s'] = TrieNode('s')
        root.children['s'].children['o'] = TrieNode('so')

        new_root = insert(root, 'bed')
        eq_(new_root.children['b'].children['e'].children['d'].data, 'bed')

        root = TrieNode('')
        new_root = insert(root, 'as')
        eq_(new_root.children['a'].data, 'a')
        eq_(new_root.children['a'].children['s'].data, 'as')

if __name__ == "__main__":
    unittest.main()