class GraphNode:
    def __init__(self, val):
        self.val = val
        self.is_visited = False
        self.adj = None


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, src, dst):
        if not src in self.nodes:
            self.nodes[src] = GraphNode(src)
        if not dst in self.nodes:
            self.nodes[dst] = GraphNode(dst)
        self.nodes[src].adj = self.nodes[dst]


def test_create_graph():
    g = Graph()
    g.add_edge('MIA', 'ORD')
    g.add_edge('DFW', 'JFK')
    g.add_edge('SFO', 'DFW')
    g.add_edge('JFK', 'MIA')

    assert g.nodes['SFO'].adj == g.nodes['DFW'] and \
        g.nodes['DFW'].adj == g.nodes['JFK'] and \
        g.nodes['JFK'].adj == g.nodes['MIA'] and \
        g.nodes['MIA'].adj == g.nodes['ORD'] and \
        g.nodes['ORD'].adj == None
