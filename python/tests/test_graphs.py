import unittest
from graphs import *
from nose.tools import eq_

class TestGraphs(unittest.TestCase):
    def test_bfs(self):
        g = {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}
        eq_(bfs(g, 0), [0, 1, 4, 5, 3, 2])

    def test_bfs_paths(self):
        g = {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}
        eq_(bfs_paths(g, 0, 4), [[0, 4], [0, 1, 4], [0, 1, 3, 4]])

    def test_find_route_bfs(self):
        g = {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}
        eq_(find_route_bfs(g, 0, 2), True)
        eq_(find_route_bfs(g, 3, 5), False)

    def test_dfs(self):
        g = {0: reversed([1, 4, 5]), 1: reversed([3, 4]), 2: [1], 3: reversed([2, 4]), 4: [], 5: []}
        eq_(dfs(g, 0), [0, 1, 3, 2, 4, 5])

    def test_check_biparty_graph(self):
        g = {0: [1, 3], 1: [0, 2, 4], 2: [1], 3: [0, 4], 4: [1, 3]}
        eq_(check_biparty_graph(g, 0), True)
        g = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}
        eq_(check_biparty_graph(g, 1), True)

    def test_dfs_r(self):
        g = {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}
        eq_(dfs_r(g, 0), [0, 1, 3, 2, 4, 5])

    def test_toplogical_sort(self):
        g = {0: [5], 1: [3, 6], 2: [5, 7], 3: [0, 7], 4: [1, 2, 6], 5: [], 6: [7], 7: [0]}
        eq_(topological_sort(g), [4, 2, 1, 6, 3, 7, 0, 5])

    def test_find_route_dfs(self):
        g = {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}
        eq_(find_route_dfs(g, 0, 2), True)
        eq_(find_route_dfs(g, 3, 5), False)

if __name__ == "__main__":
    unittest.main()
