def calc_prefix_sum(arr):
    s = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        s[i+1] = s[i] + arr[i] if i % 2 == 0 else s[i] - arr[i]
    return s


def calc_mult_prefix_sum(arr):
    ms = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        ms[i+1] = ms[i] + arr[i] * \
            (i+1) if i % 2 == 0 else ms[i] - arr[i] * (i+1)
    return ms


def calc_candy_score(s, ms, l, r):
    ret = ms[r] - ms[l-1] - (l - 1) * (s[r] - s[l-1])
    return ret if l % 2 != 0 else -ret


T = int(input())
for t in range(1, T + 1):
    N, Q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    s = calc_prefix_sum(arr)
    ms = calc_mult_prefix_sum(arr)
    ret = 0
    for q in range(Q):
        line = input().split()
        op, l, r = line[0], int(line[1]), int(line[2])
        if op == 'Q':
            ret += calc_candy_score(s, ms, l, r)
        elif op == 'U':
            arr[l-1] = r
            s = calc_prefix_sum(arr)
            ms = calc_mult_prefix_sum(arr)
    print('Case #{}: {}'.format(t, ret))
