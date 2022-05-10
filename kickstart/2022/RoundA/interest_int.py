def prod(n):
    digits = [int(d) for d in str(n)]
    ret = 1
    for d in digits:
        ret *= d
    return ret


def digit_sum(n):
    digits = [int(d) for d in str(n)]
    return sum(digits)


T = int(input())
for t in range(1, T + 1):
    A, B = list(map(int, input().split()))
    ret = 0
    for n in range(A, B + 1):
        if prod(n) % digit_sum(n) == 0:
            ret += 1
    print('Case #{}: {}'.format(t, ret))
