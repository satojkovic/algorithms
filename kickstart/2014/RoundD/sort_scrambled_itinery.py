class GraphNode:
    def __init__(self, val):
        self.val = val
        self.is_visited = False
        self.adj = None
        self.dst_node = False


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, src, dst):
        if not src in self.nodes:
            self.nodes[src] = GraphNode(src)
        if not dst in self.nodes:
            self.nodes[dst] = GraphNode(dst)
        self.nodes[src].adj = self.nodes[dst]
        self.nodes[dst].dst_node = True

    def get_root(self):
        root = None
        for k in self.nodes.keys():
            if not self.nodes[k].dst_node:
                root = self.nodes[k]
        return root


def traverse(root):
    path = []
    while root:
        path.append(root.val)
        root = root.adj
    return path


def print_path(path):
    return ' '.join([path[i] + '-' + path[i+1] for i in range(len(path) - 1)])


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

    root = g.get_root()
    assert root.val == 'SFO'


def solve():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        flights = [[input(), input()] for _ in range(N)]
        g = Graph()
        for flight in flights:
            src, dst = flight
            g.add_edge(src, dst)
        root = g.get_root()
        path = traverse(root)
        print('Case #{}: {}'.format(t, print_path(path)))


if __name__ == '__main__':
    solve()
