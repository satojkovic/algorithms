T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    Cs = list(map(int, input().split()))
    Cs_sum = sum(Cs)
    remain = Cs_sum - M * (Cs_sum // M)
    print('Case #{}: {}'.format(t, remain))
