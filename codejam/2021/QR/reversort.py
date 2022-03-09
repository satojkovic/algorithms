T = int(input())
for t in range(1, T + 1):
    N = int(input())
    L = list(map(int, input().split()))
    cost = 0
    for i in range(N - 1):
        # The input numbers are all different so the
        # minimum in each iteration is unique
        min_elem = min(L[i:N])
        j = L.index(min_elem)
        cost += (j - i + 1)
        L[i:j+1] = L[i:j+1][::-1]
    print('Case #{}: {}'.format(t, cost))
