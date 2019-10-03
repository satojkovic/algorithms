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
        self.nodes = [GraphNode(i) for i in range(6)]
        self.nodes[0].adjs.append(self.nodes[1])
        self.nodes[0].adjs.append(self.nodes[4])
        self.nodes[0].adjs.append(self.nodes[5])
        self.nodes[1].adjs.append(self.nodes[3])
        self.nodes[1].adjs.append(self.nodes[4])
        self.nodes[2].adjs.append(self.nodes[1])
        self.nodes[3].adjs.append(self.nodes[2])
        self.nodes[3].adjs.append(self.nodes[4])

    def test_bfs(self):
        eq_(bfs(self.nodes[0]), [0, 1, 4, 5, 3, 2])

    def test_dfs(self):
        eq_(dfs(self.nodes[0]), [0, 5, 4, 1, 3, 2])

    def test_dfs_r(self):
        eq_(dfs_r(self.nodes[0]), [0, 1, 3, 2, 4, 5])

if __name__ == "__main__":
    unittest.main()