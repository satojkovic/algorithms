import sys

def largest_rect_area_bf(heights):
    res = 0
    for i in range(len(heights)):
        for j in range(i, -1, -1):
            min_h = min(heights[j:i + 1])
            res = max(res, (i - j + 1) * min_h)
        res = max(res, heights[i])
    return res


def largest_rect_area_bf2(heights):
    res = 0
    for i in range(len(heights)):
        min_h = sys.maxsize
        for j in range(i, -1, -1):
            min_h = min(min_h, heights[j])
            res = max(res, (i - j + 1) * min_h)
        res = max(res, heights[i])
    return res


def largest_rect_area(heights):
    res = 0
    stack = []
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            res = max(res, height * (i - index))
            start = index
        stack.append((start, h))
    for index, height in stack:
        res = max(res, height * (len(heights) - index))
    return res


def test_largest_rect_area_bf():
    assert largest_rect_area_bf([2,1,5,6,2,3]) == 10
    assert largest_rect_area_bf([1, 4]) == 4
    assert largest_rect_area_bf([100]) == 100
    assert largest_rect_area_bf([1, 1, 1]) == 3
    assert largest_rect_area_bf([8, 0, 1, 5]) == 8
    assert largest_rect_area_bf([0, 7, 3, 4]) == 9

    assert largest_rect_area_bf2([2,1,5,6,2,3]) == 10
    assert largest_rect_area_bf2([1, 4]) == 4
    assert largest_rect_area_bf2([100]) == 100
    assert largest_rect_area_bf2([1, 1, 1]) == 3
    assert largest_rect_area_bf2([8, 0, 1, 5]) == 8
    assert largest_rect_area_bf2([0, 7, 3, 4]) == 9

def test_largest_rect_area():
    assert largest_rect_area([2,1,5,6,2,3]) == 10
    assert largest_rect_area([1, 4]) == 4
    assert largest_rect_area([100]) == 100
    assert largest_rect_area([1, 1, 1]) == 3
    assert largest_rect_area([8, 0, 1, 5]) == 8
    assert largest_rect_area([0, 7, 3, 4]) == 9
