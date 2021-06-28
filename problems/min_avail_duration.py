def min_avail_duration(slots1, slots2, duration):
    i, j = 0, 0
    res = []
    slots1.sort()
    slots2.sort()
    while i < len(slots1) and j < len(slots2):
        sect = [max(slots1[i][0], slots2[j][0]),
                min(slots1[i][1], slots2[j][1])]
        if len(sect) != 0 and sect[1] - sect[0] >= duration:
            return [sect[0], sect[0] + duration]
        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1
    return res


def test_min_avail_duration():
    assert min_avail_duration([[10, 50], [60, 80], [110, 150]], [
        [0, 15], [60, 70]], 8) == [60, 68]
