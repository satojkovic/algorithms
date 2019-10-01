#!/usr/bin/env python
# -*- coding=utf-8 -*-

class GraphNode:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adjs = []


def bfs(root):
    q = [root]
    while q:
        node = q.pop(0)
        if not node.visited:
            print(node.data)
            node.visited = True
            q = q + [node.adjs]