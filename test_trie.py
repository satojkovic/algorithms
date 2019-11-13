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

        eq_(starts_with(root, 'a' * 3), True)
        eq_(starts_with(root, 'a' * 4), False)
        eq_(starts_with(root, 'a' * 2), True)
        eq_(starts_with(root, 'a'), True)

    def test_prefix_search(self):
        root = TrieNode('')
        root = insert(root, 'apple')
        root = insert(root, 'app')
        root = insert(root, 'acdc')

        res = prefix_search(root, 'ap')
        eq_(res, ['app', 'apple'])
        res = prefix_search(root, 'x')
        eq_(res, [])
        res = prefix_search(root, 'acdc')
        eq_(res, ['acdc'])

if __name__ == "__main__":
    unittest.main()