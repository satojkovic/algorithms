#!/usr/bin/env python
# -*- coding=utf-8 -*-

from collections import deque

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.visited = False
        self.adjs = deque()

class SimpleGraph:
    def __init__(self, is_directed=True):
        self.nodes = {}
        self.is_directed = is_directed

    def add_edge(self, src, dst):
        if not src in self.nodes:
            self.nodes[src] = []
        if not dst in self.nodes:
            self.nodes[dst] = []
        self.nodes[src].append(dst)
        if not self.is_directed:
            self.nodes[dst].append(src)

    def add_vertex(self, v):
        if not v in self.nodes:
            self.nodes[v] = []

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

    def add_vertex(self, v):
        if not v in self.nodes:
            self.nodes[v] = GraphNode(v)
            self.n_vertices += 1

    # To detect cycle, find back edge by DFS
    def detect_cycle(self):
        trav_nodes = self.n_vertices * [False]
        for node_i in range(self.n_vertices):
            if not self.nodes[node_i].visited and self._detect_cycle(node_i, trav_nodes):
                return True
        return False

    def _detect_cycle(self, node_i, trav_nodes):
        # Mark current node as visited
        self.nodes[node_i].visited = True
        trav_nodes[node_i] = True

        for adj in self.nodes[node_i].adjs:
            if not adj.visited and self._detect_cycle(adj.val, trav_nodes):
                return True
            elif trav_nodes[adj.val]:
                return True

        trav_nodes[node_i] = False
        return False

# graph is represented as an adjacency matrix
# g = {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}

def bfs(g, root):
    # Initialize `visited` with an empty list to return result as a list
    q, seen, visited = deque([root]), {root}, []
    while q:
        node = q.popleft()
        visited.append(node)
        for adj in g[node]:
            if not adj in seen:
                seen.add(adj)
                q.append(adj)
    return visited

def find_route_bfs(start, end):
    q = deque([start])
    start.visited = True
    while q:
        node = q.popleft()
        if node.val == end.val:
            return True
        for adj in node.adjs:
            if not adj.visited:
                q.append(adj)
                adj.visited = True
    return False

def find_route_dfs(start, end):
    if start.val == end.val:
        return True
    start.visited = True
    for adj in start.adjs:
        if not adj.visited:
            return find_route_dfs(adj, end)
    return False

def bfs_paths(g, root, target):
    q = deque([(root, set(), [])])
    paths = []
    while q:
        node, visited, path = q.popleft()
        if node == target:
            paths.append(path + [node])
            continue
        if not node in visited:
            visited = visited | {node}
            path = path + [node]
            for adj in g[node]:
                q.append((adj, visited, path))
    return paths

def dfs(g, root):
    stack, seen, visited = [root], {root}, []
    while stack:
        node = stack.pop()
        visited.append(node)
        for adj in g[node]:
            if not adj in seen:
                stack.append(adj)
                seen.add(adj)
    return visited

def dfs_r(g, root):
    def _dfs_r(g, root, visited, path):
        if root in visited:
            return path
        visited.add(root)
        path.append(root)
        for adj in g[root]:
            if not adj in visited:
                path = _dfs_r(g, adj, visited, path)
        return path
    visited, path = set(), []
    return _dfs_r(g, root, visited, path)

if __name__ == "__main__":
    g = SimpleGraph(is_directed=False)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(4, 5)
    for node in g.nodes:
        print(node, '->', ','.join([str(n) for n in g.nodes[node]]))
    g.add_vertex(10)
    print('nodes:', ','.join([str(node) for node in g.nodes]))
    print('dfs:', dfs(g.nodes, 0))
    print('dfs_r:', dfs_r(g.nodes, 0))

    g = {}
    a = GraphNode('a')
    b = GraphNode('b')
    c = GraphNode('c')
    d = GraphNode('d')
    e = GraphNode('e')
    f = GraphNode('f')
    g = GraphNode('g')
    a.adjs.append(b)
    a.adjs.append(c)
    b.adjs.append(a)
    b.adjs.append(d)
    c.adjs.append(a)
    c.adjs.append(g)
    d.adjs.append(b)
    d.adjs.append(e)
    e.adjs.append(d)
    f.adjs.append(d)

    print(find_route_dfs(c, e))