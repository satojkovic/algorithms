import heapq
from typing import List


def kClosest_sort(points: List[List[int]], k: int) -> List[List[int]]:
    points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
    return points[:k]


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    for point in points:
        dist_sq = point[0] ** 2 + point[1] ** 2
        if len(heap) < k:
            heapq.heappush(heap, (-dist_sq, point))
        else:
            if -dist_sq > heap[0][0]:
                heapq.heapreplace(heap, (-dist_sq, point))
    return [point for dist_sq, point in heap]


def test_k_closest():
    import deepdiff

    assert not deepdiff.DeepDiff(
        kClosest_sort([[1, 3], [-2, 2]], 1), [[-2, 2]], ignore_order=True
    )
    assert not deepdiff.DeepDiff(
        kClosest_sort([[1, 3], [-2, 2]], 2), [[-2, 2], [1, 3]], ignore_order=True
    )

    assert not deepdiff.DeepDiff(
        kClosest([[1, 3], [-2, 2]], 1), [[-2, 2]], ignore_order=True
    )
    assert not deepdiff.DeepDiff(
        kClosest([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]], ignore_order=True
    )
