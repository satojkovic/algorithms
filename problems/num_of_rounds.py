def num_of_rounds(startTime, finishTime):
    import math
    start = int(startTime[:2]) * 60 + int(startTime[3:])
    finish = int(finishTime[:2]) * 60 + int(finishTime[3:])
    if start > finish:
        finish += 24 * 60
    return max(0, math.floor(finish/15) - math.ceil(start/15))


def test_num_of_rounds():
    assert num_of_rounds('12:10', '13:00') == 3
    assert num_of_rounds('20:00', '06:00') == 40
    assert num_of_rounds('00:00', '23:59') == 95
