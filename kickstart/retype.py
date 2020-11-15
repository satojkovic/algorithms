# Test input:
# 2
# 10 5 2
# 10 7 6
# Test output:
# Case #1: 15
# Case #2: 12

T = int(input())
for i in range(1, T + 1):
    N, K, S = list(map(int, input().split()))
    common = K - 1
    res = min(common + N + 1, common + (K - S) + (N - S) + 1)
    print('Case #{}: {}'.format(i, res))