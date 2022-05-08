def get_min_max_pressure(n):
    min_max_ps = []
    for _ in range(n):
        ps = list(map(int, input().split()))
        min_max_ps.append([min(ps), max(ps)])
    return min_max_ps


T = int(input())
for t in range(1, T + 1):
    N, P = list(map(int, input().split()))
    min_max_ps = get_min_max_pressure(N)
    dp = [[0, 0] for _ in range(N + 1)]
    l0, l1 = 0, 0
    for i, min_max_p in enumerate(min_max_ps):
        min_p, max_p = min_max_p
        diff_min_max_p = max_p - min_p
        dp[i+1][0] = min(
            dp[i][0] + abs(l0 - min_p) + diff_min_max_p,
            dp[i][1] + abs(l1 - min_p) + diff_min_max_p
        )
        dp[i+1][1] = min(
            dp[i][0] + abs(l0 - max_p) + diff_min_max_p,
            dp[i][1] + abs(l1 - max_p) + diff_min_max_p
        )
        l0 = max_p
        l1 = min_p
    print('Case #{}: {}'.format(t, min(dp[N][0], dp[N][1])))
