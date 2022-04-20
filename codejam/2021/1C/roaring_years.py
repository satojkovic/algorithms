def get_roaring_years():
    import math
    ret = []
    for i in range(1, 10**6):
        y = i
        y_len = int(math.log10(y) + 1)
        digit = i
        while y_len < 20:
            digit += 1
            digit_len = int(math.log10(digit) + 1)
            y_len += digit_len
            y = y * 10 ** digit_len + digit
            ret.append(y)
    return sorted(ret)


def concat(x):
    import math
    digit_len = int(math.log10(x + 1) + 1)
    return x * (10**digit_len) + (x + 1)


def binary_search_two(y):
    left = 0
    right = 10**9 - 1
    while right - left > 1:
        mid = left + (right - left) // 2
        if concat(mid) > y:
            right = mid
        else:
            left = mid
    return concat(right)


def binary_search_three(y, years):
    left = -1
    right = len(years) - 1
    while right - left > 1:
        mid = left + (right - left) // 2
        if years[mid] > y:
            right = mid
        else:
            left = mid
    return years[right]


T = int(input())
for t in range(1, T + 1):
    Y = int(input())
    roaring_years = get_roaring_years()
    print('Case #{}: {}'.format(
        t, min(binary_search_two(Y), binary_search_three(Y, roaring_years)
               )))
