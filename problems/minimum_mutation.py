def minimum_mutation(start, end, bank):
    from collections import deque
    q = deque([(start, 0)])
    visited = set()
    visited.add(start)
    bank_set = set(bank)
    while q:
        node, level = q.popleft()
        if node == end:
            return level
        for i, _ in enumerate(node):
            for gene in ['A', 'C', 'G', 'T']:
                new_gene_str = node[:i] + gene + node[i+1:]
                if not new_gene_str in visited and new_gene_str in bank_set:
                    visited.add(new_gene_str)
                    q.append((new_gene_str, level + 1))
    return -1
