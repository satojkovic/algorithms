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


def solve1():
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


def calc_score(l, r, N):
    if r == 0:
        return 0
    elif l == -1:
        return (r * (r + 1)) // 2
    elif r == -1:
        return ((N-l-1) * (N-l)) // 2
    else:
        zero_count = r - l - 1
        if zero_count == 1:
            return 1
        elif zero_count == 2:
            return 2
        else:
            n = zero_count // 2
            return n * (n+1) if zero_count % 2 == 0 else n * (n+1) + (n+1)


def solve2():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        trash_bins = input()
        trash_bins = list(map(int, [c for c in trash_bins]))
        l = -1
        ret = 0
        for r in range(N):
            if trash_bins[r] == 1:
                ret += calc_score(l, r, N)
                l = r
        print('Case #{}: {}'.format(t, ret if l ==
              N - 1 else ret + calc_score(l, -1, N)))


if __name__ == '__main__':
    solve2()
