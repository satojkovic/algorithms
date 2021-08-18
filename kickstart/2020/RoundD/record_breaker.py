T = int(input())
for t in range(1, T + 1):
    N = int(input())
    visitors = list(map(int, input().split(' ')))
    prev_record = 0
    res = 0
    for i in range(N):
        greater_than_prev = i == 0 or visitors[i] > prev_record
        greater_than_next = i == N - 1 or visitors[i] > visitors[i + 1]
        res = res + 1 if greater_than_prev and greater_than_next else res
        prev_record = max(prev_record, visitors[i])
    print('Case #{}: {}'.format(t, res))
