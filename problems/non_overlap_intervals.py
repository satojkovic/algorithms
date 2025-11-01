from typing import List

def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    removed_count = 0
    prev_end = sorted_intervals[0][1]
    for i in range(1, len(sorted_intervals)):
        curr_start = sorted_intervals[i][0]
        curr_end = sorted_intervals[i][1]
        if prev_end > curr_start:
            removed_count += 1
            prev_end = min(prev_end, curr_end)
        else:
            prev_end = curr_end
    return removed_count


def test_eraseOverlapIntervals():
    assert eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    assert eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
    assert eraseOverlapIntervals([[1,2],[2,3]]) == 0
    assert eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]) == 2
    assert eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]) == 2