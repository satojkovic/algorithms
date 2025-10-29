from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    i = 0
    N = len(intervals)

    while i < N and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    while i < N and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    while i < N:
        result.append(intervals[i])
        i += 1

    return result


def test_insert():
    assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    assert insert([], [5,7]) == [[5,7]]
    assert insert([[1,5]], [2,3]) == [[1,5]]
    assert insert([[1,5]], [6,8]) == [[1,5],[6,8]]
    assert insert([[1,5]], [0,0]) == [[0,0],[1,5]]
    assert insert([[1,5]], [0,3]) == [[0,5]]
    assert insert([[1,5]], [0,6]) == [[0,6]]
    assert insert([[3,5],[12,15]], [6,8]) == [[3,5],[6,8],[12,15]]
    assert insert([[1,2],[3,4],[5,6]], [7,8]) == [[1,2],[3,4],[5,6],[7,8]]
