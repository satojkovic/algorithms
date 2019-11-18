import unittest
from trie import *
from nose.tools import eq_

class TestTrie(unittest.TestCase):
    def test_insert_search(self):
        trie = Trie()
        trie.insert('a' * 3)
        eq_(trie.root.children['a'].children['a'].children['a'].word_finished, True)
        eq_(trie.root.children['a'].children['a'].word_finished, False)
        trie.insert('a' * 2)
        eq_(trie.root.children['a'].children['a'].word_finished, True)

        eq_(trie.search('a' * 3), True)
        eq_(trie.search('a' * 4), False)
        eq_(trie.search('a' * 2), True)
        eq_(trie.search('a'), False)

        eq_(trie.starts_with('a' * 3), True)
        eq_(trie.starts_with('a' * 4), False)
        eq_(trie.starts_with('a' * 2), True)
        eq_(trie.starts_with('a'), True)

    def test_prefix_search(self):
        trie = Trie()
        trie.insert('apple')
        trie.insert('app')
        trie.insert('acdc')

        res = trie.prefix_search('ap')
        eq_(res, ['app', 'apple'])
        res = trie.prefix_search('x')
        eq_(res, [])
        res = trie.prefix_search('acdc')
        eq_(res, ['acdc'])

if __name__ == "__main__":
    unittest.main()