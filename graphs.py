#!/usr/bin/env python
# -*- coding=utf-8 -*-

class GraphNode:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adjs = []


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

