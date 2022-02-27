def my_sqrt(x):
    # Upper bound search
    left, right = 0, x + 1
    while right - left > 1:
        mid = left + (right - left) // 2
        if mid ** 2 <= x:
            left = mid
        else:
            right = mid
    return left


def test_mysqrt():
    # 0 <= x
    assert my_sqrt(10) == 3
    assert my_sqrt(0) == 0
    assert my_sqrt(1) == 1
