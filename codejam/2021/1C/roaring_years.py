def get_roaring_years():
    import math
    ret = []
    for i in range(1, 1000):
        y = i
        digit = i
        while y < 1234567:
            digit += 1
            digit_len = int(math.log10(digit) + 1)
            y = y * 10 ** digit_len + digit
            ret.append(y)
    return sorted(ret)


def linear_search(y, years):
    ret = 1234567
    for year in years:
        if year > y:
            ret = year
            break
    return ret


T = int(input())
for t in range(1, T + 1):
    Y = int(input())
    roaring_years = get_roaring_years()
    print('Case #{}: {}'.format(t, linear_search(Y, roaring_years)))
