#!/usr/bin/env python
# -*- coding=utf-8 -*-

from collections import deque

class GraphNode:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adjs = deque()
        self.n_vertices = 0

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, src, dst):
        if not src in self.nodes:
            self.nodes[src] = GraphNode(src)
            self.n_vertices += 1
        if not dst in self.nodes:
            self.nodes[dst] = GraphNode(dst)
            self.n_vertices += 1

        self.nodes[src].adjs.append(self.nodes[dst])


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
