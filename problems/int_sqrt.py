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