#!/usr/bin/env python
# -*- coding=utf-8 -*-

from collections import deque

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.adjs = deque()

class Graph:
    def __init__(self) -> None:
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
            self.n_vetices += 1

def find_mother_vertex(g):
    def dfs(root):
        s = deque([root])
        visited = [root.val]
        while s:
            node = s.popleft()
            for adj in node.adjs:
                if not adj.val in visited:
                    visited.append(adj.val)
                    s.appendleft(adj)
        return visited

    res = []
    for node in g.nodes.keys():
        visited = dfs(g.nodes[node])
        if len(visited) == len(list(g.nodes.keys())):
            res.append(node)
    return res