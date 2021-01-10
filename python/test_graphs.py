import unittest
from graphs import *
from nose.tools import eq_

class TestGraphs(unittest.TestCase):
    def test_bfs(self):
        g = {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}
        eq_(bfs(g, 0), [0, 1, 4, 5, 3, 2])
        eq_(bfs2(g, 0), [0, 1, 4, 5, 3, 2])

    def test_bfs_paths(self):
        g = {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}
        eq_(bfs_paths(g, 0, 4), [[0, 4], [0, 1, 4], [0, 1, 3, 4]])

    def test_dfs(self):
        g = {0: reversed([1, 4, 5]), 1: reversed([3, 4]), 2: [1], 3: reversed([2, 4]), 4: [], 5: []}
        eq_(dfs(g, 0), [0, 1, 3, 2, 4, 5])

    def test_dfs_r(self):
        g = {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}
        eq_(dfs_r(g, 0), [0, 1, 3, 2, 4, 5])

if __name__ == "__main__":
    unittest.main()