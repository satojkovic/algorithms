import math


class SegmentTreeSum:
    def __init__(self, arr=None, is_mult=False):
        if arr:
            self.build(arr)
        self.is_mult = is_mult

    def build(self, arr):
        def _build(curr, arr, left, right):
            if left == right:
                self.data[curr] = arr[left]
            else:
                mid = (left + right) // 2
                _build(2 * curr + 1, arr, left, mid)
                _build(2 * curr + 2, arr, mid + 1, right)
                self.data[curr] = self.data[2 * curr + 1] + \
                    self.data[2 * curr + 2]
        self.n = len(arr)
        x = 2 ** math.ceil(math.log2(self.n))
        self.data = [0] * (2 * x - 1)
        _build(0, arr, 0, self.n - 1)

    def update(self, i, x):
        def _update(i, x, curr, left, right):
            if left == right:
                if self.is_mult:
                    self.data[curr] = x * (i+1) if i % 2 == 0 else -x * (i+1)
                else:
                    self.data[curr] = x if i % 2 == 0 else -x
            else:
                mid = (left + right) // 2
                if mid >= i:
                    _update(i, x, 2 * curr + 1, left, mid)
                else:
                    _update(i, x, 2 * curr + 2, mid + 1, right)
                self.data[curr] = self.data[2 * curr + 1] + \
                    self.data[2 * curr + 2]

        _update(i, x, 0, 0, self.n - 1)

    def query(self, range_l, range_r):
        def _query(curr, left, right, range_l, range_r):
            if right < range_l or range_r < left:
                return 0
            if range_l <= left and right <= range_r:
                return self.data[curr]
            mid = (left + right) // 2
            left_sum = _query(2 * curr + 1, left, mid, range_l, range_r)
            right_sum = _query(2 * curr + 2, mid + 1,
                               right, range_l, range_r)
            return left_sum + right_sum

        return _query(0, 0, self.n - 1, range_l, range_r)


def calc_prefix_sum(arr):
    s = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        s[i+1] = s[i] + arr[i] if i % 2 == 0 else s[i] - arr[i]
    return s


def calc_mult_prefix_sum(arr):
    ms = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        ms[i+1] = ms[i] + arr[i] * \
            (i+1) if i % 2 == 0 else ms[i] - arr[i] * (i+1)
    return ms


def calc_candy_score(s, ms, l, r):
    ret = ms[r] - ms[l-1] - (l - 1) * (s[r] - s[l-1])
    return ret if l % 2 != 0 else -ret


T = int(input())
for t in range(1, T + 1):
    N, Q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    s = [a if i % 2 == 0 else -a for i, a in enumerate(arr)]
    ms = [a * (i+1) if i % 2 == 0 else -a * (i+1) for i, a in enumerate(arr)]
    st_s = SegmentTreeSum(s)
    st_ms = SegmentTreeSum(ms, is_mult=True)
    ret = 0
    for _ in range(Q):
        line = input().split()
        op, l, r = line[0], int(line[1]), int(line[2])
        if op == 'Q':
            q = (-1) ** (l-1) * (st_ms.query(l-1, r-1) -
                                 (l-1) * st_s.query(l-1, r-1))
            ret += int(q)
        elif op == 'U':
            st_s.update(l-1, r)
            st_ms.update(l-1, r)
    print('Case #{}: {}'.format(t, ret))
