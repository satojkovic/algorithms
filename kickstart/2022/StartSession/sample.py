T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))
    Cs = list(map(int, input().split()))
    remain = sum(Cs) % M
    print('Case #{}: {}'.format(t, remain))
