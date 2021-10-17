T = int(input())
for t in range(1, T + 1):
    N, D, C, M = list(map(int, input().split()))
    S = input().strip()
    n_dogs = sum([1 for c in S if c == 'D'])
    if n_dogs == 0:
        print('Case #{}: YES'.format(t))
        continue
    cond = True
    for c in S:
        if c == 'D':
            if D == 0:
                cond = False
            else:
                D -= 1
                C += M
                n_dogs -= 1
        elif c == 'C':
            if C == 0:
                cond = False
            else:
                C -= 1
        if cond is False:
            break
        if n_dogs == 0:
            break
    res = 'YES' if cond else 'NO'
    print('Case #{}: {}'.format(t, res))
