#!/usr/bin/env python
# -*- coding=utf-8 -*-

from collections import deque

class GraphNode:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adjs = deque()

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
            if not adj.visited and self._detect_cycle(adj.data, trav_nodes):
                return True
            elif trav_nodes[adj.data]:
                return True

        trav_nodes[node_i] = False
        return False

def bfs(root, path=[]):
    root.visited = True
    q = deque([root])
    while q:
        node = q.popleft()
        path.append(node.data)
        for adj in node.adjs:
            if not adj.visited:
                adj.visited = True
                q.append(adj)
    return path

def dfs(root, path=[]):
    root.visited = True
    s = deque([root])
    while s:
        node = s.popleft()
        path.append(node.data)
        # Last node of the adjacency list is the first node of next while loop
        for adj in node.adjs:
            if not adj.visited:
                adj.visited = True
                s.appendleft(adj)
    return path

def dfs_r(root):
    def helper(root, path):
        if root is None or root.visited:
            return path
        root.visited = True
        path.append(root.data)
        for adj in root.adjs:
            path = helper(adj, path)
        return path

    path = []
    path = helper(root, path)
    return path

def dfs_r2(root):
    if root is None or root.visited:
        return []
    root.visited = True
    path = [root.data]
    for adj in root.adjs:
        adj_path = dfs_r2(adj)
        path += adj_path
    return path
