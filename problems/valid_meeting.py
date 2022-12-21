def valid_meeting(intervals):
    intervals = sorted(intervals, key=lambda x: x[1])
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i+1][0]:
            return False
    return True


def test_valid_meeting():
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert not valid_meeting(intervals)
    intervals = [[7, 10], [2, 4]]
    assert valid_meeting(intervals)
    
    intervals = []
    assert valid_meeting(intervals)
    intervals = [[1, 3]]
    assert valid_meeting(intervals)
    intervals = [[1, 1], [1, 1]]
    assert valid_meeting(intervals)

