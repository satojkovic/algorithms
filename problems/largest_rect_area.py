def largest_rect_area_bf(heights):
    res = 0
    for i in range(len(heights)):
        for j in range(i, -1, -1):
            min_h = min(heights[j:i + 1])
            res = max(res, (i - j + 1) * min_h)
        res = max(res, heights[i])
    return res


def test_largest_rect_area_bf():
    assert largest_rect_area_bf([2,1,5,6,2,3]) == 10
    assert largest_rect_area_bf([1, 4]) == 4
    assert largest_rect_area_bf([100]) == 100
    assert largest_rect_area_bf([1, 1, 1]) == 3
    assert largest_rect_area_bf([8, 0, 1, 5]) == 8
    assert largest_rect_area_bf([0, 7, 3, 4]) == 9
