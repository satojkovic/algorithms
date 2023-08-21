from collections import defaultdict, deque


def valid_path(n, edges, source, destination):
    dict_edges = convert_to_dict(edges)
    q = deque([source])
    seen = set([source])
    while q:
        node = q.pop()
        if node == destination:
            return True
        for v in dict_edges[node]:
            if v not in seen:
                q.appendleft(v)
                seen.add(v)
    return False


def convert_to_dict(edges):
    dict_edges = defaultdict(list)
    for edge in edges:
        u, v = edge
        dict_edges[u].append(v)
        dict_edges[v].append(u)
    return dict_edges


def test_valid_path():
    assert valid_path(3, [[0, 1], [1, 2], [0, 2]], 0, 2) == True
    assert valid_path(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) == False
    assert valid_path(1, [], 0, 0) == True
