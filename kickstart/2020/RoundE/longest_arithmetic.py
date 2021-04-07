T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    diffs = []
    for i in range(1, N):
        diffs.append(nums[i] - nums[i-1])
    curr = diffs[0]
    res = 1
    max_res = 0
    for i in range(1, len(diffs)):
        if diffs[i] == curr:
            res += 1
        else:
            max_res = res if res > max_res else max_res
            res = 1
            curr = diffs[i]
    print('Case #{}: {}'.format(t, max_res + 1 if max_res > res else res + 1))
