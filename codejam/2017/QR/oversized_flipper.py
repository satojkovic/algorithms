T = int(input())
for t in range(1, T + 1):
    S, K = input().split()
    S = list(S)
    K = int(K)
    N = len(S)
    res = 0
    for i in range(N - K + 1):
        if S[i] == '-':
            for k in range(K):
                S[i+k] = '+' if S[i+k] == '-' else '-'
            res += 1
    res = res if all([True if s == '+' else False for s in S]
                     ) else 'IMPOSSIBLE'
    print('Case #{}: {}'.format(t, res))
