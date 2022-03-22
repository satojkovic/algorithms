# Sub sequence check can be done in O(M) with constant extra space.
def is_subsequence(I, P):
    N = len(I)
    M = len(P)
    i, j = 0, 0
    while i < len(I) and j < len(P):
        if I[i] == P[j]:
            i += 1
            j += 1
        else:
            j += 1
    return True if i == N else False


T = int(input())
for t in range(1, T + 1):
    I = input().rstrip()
    P = input().rstrip()
    if is_subsequence(I, P):
        print('Case #{}: {}'.format(t, len(P) - len(I)))
    else:
        print('Case #{}: IMPOSSIBLE'.format(t))
