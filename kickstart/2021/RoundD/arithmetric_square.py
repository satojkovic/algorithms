def check(arr):
    return (arr[1] - arr[0]) == (arr[2] - arr[1])


def get_outside_col(top, mid, bottom):
    return [[top[0], mid[0], bottom[0]], [top[2], mid[1], bottom[2]]]


def get_unknown(top, mid, bottom):
    return [[top[0], bottom[2]], [bottom[0], top[2]], [top[1], bottom[1]], [mid[0], mid[1]]]


T = int(input())
for t in range(1, T + 1):
    top = list(map(int, input().split()))
    mid = list(map(int, input().split()))
    bottom = list(map(int, input().split()))

    res = 0
    res = res + 1 if check(top) else res
    res = res + 1 if check(bottom) else res
    cols = get_outside_col(top, mid, bottom)
    for col in cols:
        res = res + 1 if check(col) else res
    unknowns = get_unknown(top, mid, bottom)
    m = {}
    for unknown in unknowns:
        diff = abs(unknown[1] - unknown[0])
        if diff % 2 == 0:
            x = min(unknown) + diff // 2
            if x in m:
                m[x] += 1
            else:
                m[x] = 1
    if m:
        res += max([c for x, c in m.items()])
    print('Case #{}: {}'.format(t, res))
