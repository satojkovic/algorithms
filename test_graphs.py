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

        # "A": ["B", "C"],
        # "B": ["A", "D", "E"],
        # "C": ["A", "F"],
        # "D": ["B"],
        # "E": ["B", "F"],
        # "F": ["C", "E"],
        self.graph2 = Graph()
        self.graph2.add_edge('A', 'B')
        self.graph2.add_edge('A', 'C')
        self.graph2.add_edge('B', 'A')
        self.graph2.add_edge('B', 'D')
        self.graph2.add_edge('B', 'E')
        self.graph2.add_edge('C', 'A')
        self.graph2.add_edge('C', 'F')
        self.graph2.add_edge('D', 'B')
        self.graph2.add_edge('E', 'B')
        self.graph2.add_edge('E', 'F')
        self.graph2.add_edge('F', 'C')
        self.graph2.add_edge('F', 'E')

    def test_bfs(self):
        eq_(bfs(self.graph.nodes[0], path=[]), [0, 1, 4, 5, 3, 2])
        eq_(bfs(self.graph2.nodes['A'], path=[]), ['A', 'B', 'C', 'D', 'E', 'F'])

    def test_dfs(self):
        eq_(dfs(self.graph.nodes[0]), [0, 5, 4, 1, 3, 2])

    def test_dfs_r(self):
        eq_(dfs_r(self.graph.nodes[0]), [0, 1, 3, 2, 4, 5])

    def test_dfs_r2(self):
        eq_(dfs_r2(self.graph.nodes[0]), [0, 1, 3, 2, 4, 5])

    def test_detect_cycle_from_node(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(0, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 3)
        eq_(g.detect_cycle(), True)

        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        eq_(g.detect_cycle(), False)

        g = Graph()
        g.add_edge(0, 0)
        eq_(g.detect_cycle(), True)

if __name__ == "__main__":
    unittest.main()