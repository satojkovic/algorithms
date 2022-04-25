T = int(input())
for t in range(1, T + 1):
    N = int(input())
    ps = list(map(int, input().split()))
    left, right = 0, N - 1
    ret = 0
    prev_max = None
    while left <= right:
        curr = min(ps[left], ps[right])
        if ps[left] >= ps[right]:
            right -= 1
        else:
            left += 1
        if prev_max is None or prev_max <= curr:
            ret += 1
        prev_max = max(curr, prev_max) if prev_max is not None else curr
    print('Case #{}: {}'.format(t, ret))
