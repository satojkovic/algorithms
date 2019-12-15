import unittest
from graphs import *
from nose.tools import eq_

class TestGraphs(unittest.TestCase):
    def setUp(self):
        # 0: [1, 4, 5]
        # 1: [3, 4]
        # 2: [1]
        # 3: [2, 4]
        # 4: []
        # 5: []
        self.graph = Graph()
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 4)
        self.graph.add_edge(0, 5)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(1, 4)
        self.graph.add_edge(2, 1)
        self.graph.add_edge(3, 2)
        self.graph.add_edge(3, 4)

    def test_bfs(self):
        eq_(bfs(self.graph.nodes[0]), [0, 1, 4, 5, 3, 2])

    def test_dfs(self):
        eq_(dfs(self.graph.nodes[0]), [0, 5, 4, 1, 3, 2])

    def test_dfs_r(self):
        eq_(dfs_r(self.graph.nodes[0]), [0, 1, 3, 2, 4, 5])

    def test_dfs_r2(self):
        eq_(dfs_r2(self.graph.nodes[0]), [0, 1, 3, 2, 4, 5])

if __name__ == "__main__":
    unittest.main()