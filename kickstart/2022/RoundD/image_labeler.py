T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    As = list(map(int, input().split()))
    As = sorted(As, reverse=True)
    res = 0
    for i in range(M-1):
        res += As[i]

    rem = [As[i] for i in range(N-1, M-2, -1)]
    if len(rem) % 2 != 0:
        res += rem[len(rem) // 2]
    else:
        med = (rem[len(rem) // 2] + rem[len(rem) // 2 - 1]) / 2
        res += med

    print('Case #{}: {}'.format(t, res))
