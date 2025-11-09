from collections import defaultdict
import heapq
from typing import List

def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    adj = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))

    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[k] = 0

    priority_queue = [(0, k)]

    while priority_queue:
        dist, node = heapq.heappop(priority_queue)
        if distances[node] < dist:
            continue
        for v, w in adj[node]:
            new_dist = dist + w
            if new_dist < distances[v]:
                distances[v] = new_dist
                heapq.heappush(priority_queue, (new_dist, v))

    max_dist = max(distances.values())
    return int(max_dist) if max_dist != float('inf') else -1


def test_networkDelayTime():
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    assert networkDelayTime(None, times, n, k) == 2

    times = [[1, 2, 1]]
    n = 2
    k = 1
    assert networkDelayTime(None, times, n, k) == 1

    times = [[1, 2, 1]]
    n = 2
    k = 2
    assert networkDelayTime(None, times, n, k) == -1

    times = [[1, 2, 1], [2, 3, 2], [1, 3, 2]]
    n = 3
    k = 1
    assert networkDelayTime(None, times, n, k) == 2
