from collections import deque

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.adjs = deque()
        self.visited = False

class Graph:
    def __init__(self):
        self.nodes = {}
        self.n_vertices = 0

    def add_edge(self, src, dst):
        if not src in self.nodes:
            self.nodes[src] = GraphNode(src)
            self.n_vertices += 1
        if not dst in self.nodes:
            self.nodes[dst] = GraphNode(dst)
            self.n_vertices += 1
        self.nodes[src].adjs.appendleft(self.nodes[dst])

def find_shortest_path(root, target):
    q = deque([root])
    root.visited = True
    steps = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.val == target.val:
                return steps
            for adj in node.adjs:
                if not adj.visited:
                    q.append(adj)
                    adj.visited = True
        steps += 1        
    return -1