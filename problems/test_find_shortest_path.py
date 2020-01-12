import unittest
from find_shortest_path import *
from nose.tools import eq_

class TestFindShortestPath(unittest.TestCase):
    def test_find_shortest_path(self):
        g = Graph()
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('A', 'D')
        g.add_edge('B', 'E')
        g.add_edge('C', 'E')
        g.add_edge('C', 'F')
        g.add_edge('D', 'G')
        eq_(find_shortest_path(g.nodes['A'], g.nodes['G']), 2)
        eq_(find_shortest_path(g.nodes['A'], g.nodes['A']), 0)
        eq_(find_shortest_path(g.nodes['E'], g.nodes['F']), -1)

if __name__ == "__main__":
    unittest.main()