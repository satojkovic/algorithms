import numpy as np
T = int(input())
for t in range(1, T + 1):
    S = input().strip()
    F = input().strip()
    dist = []
    for i, cf in enumerate(F):
        dist.append(
            [min(abs(ord(cf) - ord(cs)), 25 - abs(ord(cf) - ord(cs)) + 1) for cs in S])
    res = 0
    for i in range(len(S)):
        res += min(np.array(dist)[:, i])
    print('Case #{}: {}'.format(t, res))
