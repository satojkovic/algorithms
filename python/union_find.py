#!/usr/bin/env python
# -*- coding=utf-8 -*-

class UnionFind:
    def __init__(self, size):
        self.size = size
        self.num_components = self.size
        # Each component is originally of size 1
        self.sz = [1 for i in range(self.size)]
        # Link to itself
        self.id = [i for i in range(self.size)]

    # Find which component/set 'p' belongs to, takes amortized constant time.
    def find(self, p):
        # Find the root of the component/set
        root = p
        while root != self.id[root]:
            root = self.id[root]

        # Compress the path leading back to the root = Path compression
        while p != root:
            next_ = self.id[p]
            self.id[p] = root
            p = next_

        return root

    # Return whether or not the components 'p' and 'q' are in the same component/set
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # Return the size of the component/set 'p' belongs to
    def component_size(self, p):
        return self.sz[self.find(p)]

    # Unify the components/sets containing elements 'p' and 'q'
    def unify(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        
        # These elements are already in the same group
        if rootp == rootq:
            return
        
        # Merge two components/sets together
        # Merge smaller component/set into the larger one
        if self.sz[rootp] < self.sz[rootq]:
            self.sz[rootq] += self.sz[rootp]
            self.id[rootp] = rootq
        else:
            self.sz[rootp] += self.sz[rootq]
            self.id[rootq] = rootp

        self.num_components -= 1

if __name__ == "__main__":
    sz = 7
    uf = UnionFind(sz)
    uf.unify(0, 2)
    print('num components:', uf.num_components)
    print([uf.component_size(i) for i in range(sz)])
    print('connected 0 to 2:', uf.connected(0, 2))
    print('connected 2 to 0:', uf.connected(2, 0))
    print('connected 1 to 3:', uf.connected(1, 3))
    print('connected 3 to 1:', uf.connected(3, 1))
    print('connected 6 to 4:', uf.connected(6, 4))
    uf.unify(3, 1)
    print('num components:', uf.num_components)
    print([uf.component_size(i) for i in range(sz)])
    print('connected 0 to 2:', uf.connected(0, 2))
    print('connected 2 to 0:', uf.connected(2, 0))
    print('connected 1 to 3:', uf.connected(1, 3))
    print('connected 3 to 1:', uf.connected(3, 1))
    print('connected 6 to 4:', uf.connected(6, 4))
