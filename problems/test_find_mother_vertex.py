import unittest
from find_mother_vertex import *
from nose.tools import eq_

class TestFindMotherVertex(unittest.TestCase):
    def test_find_mother_vertex(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        eq_(find_mother_vertex(g), [0, 1, 2])

        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(3, 1)
        g.add_edge(3, 0)
        g.add_vertex(2)
        eq_(find_mother_vertex(g), [3])

if __name__ == "__main__":
    unittest.main()
