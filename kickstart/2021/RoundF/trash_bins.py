def left_diff(trash_bins, i):
    left = i - 1
    while left >= 0:
        if trash_bins[left] == 1:
            break
        left -= 1
    return N if left == -1 else abs(left - i)


def right_diff(trash_bins, i):
    right = i + 1
    while right < len(trash_bins):
        if trash_bins[right] == 1:
            break
        right += 1
    return N if right == len(trash_bins) else abs(right - i)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    trash_bins = input()
    trash_bins = list(map(int, [c for c in trash_bins]))
    ret = 0
    for i in range(N):
        if trash_bins[i] == 1:
            continue
        l = left_diff(trash_bins, i)
        r = right_diff(trash_bins, i)
        ret += min(l, r)
    print('Case #{}: {}'.format(t, ret))
