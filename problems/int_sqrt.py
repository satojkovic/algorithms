def approx_sqrt(x):
    if x < 2:
        return x
    lo = 2
    hi = x // 2
    while lo <= hi:
        mid = (lo + hi) // 2
        n = mid * mid
        if n > x:
            hi = mid - 1
        elif n < x:
            lo = mid + 1
        else:
            return mid
    return hi


def test_approx_sqrt():
    assert approx_sqrt(4) == 2
    assert approx_sqrt(15) == 3
    assert approx_sqrt(1) == 1
