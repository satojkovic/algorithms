#!/usr/bin/env python
# -*- coding=utf-8 -*-

class GraphNode:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adjs = []

    def add_adjacent(self, adj):
        self.adjs.append(adj)

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, src, dst):
        if not src in self.nodes:
            self.nodes[src] = GraphNode(src)
        if not dst in self.nodes:
            self.nodes[dst] = GraphNode(dst)

        self.nodes[src].add_adjacent(self.nodes[dst])


def bfs(root, path=[]):
    root.visited = True
    q = [root]
    while q:
        node = q.pop(0)
        path.append(node.data)
        for adj in node.adjs:
            if not adj.visited:
                adj.visited = True
                q = q + [adj]
    return path

def dfs(root, path=[]):
    root.visited = True
    s = [root]
    while s:
        node = s.pop(0)
        path.append(node.data)
        # Last node of the adjacency list is the first node of next while loop
        for adj in node.adjs:
            if not adj.visited:
                adj.visited = True
                s = [adj] + s
    return path

def dfs_r(root):
    def helper(root, path):
        if root.visited:
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
    if root.visited:
        return []
    root.visited = True
    path = [root.data]
    for adj in root.adjs:
        adj_path = dfs_r2(adj)
        path += adj_path
    return path

