import math


class SegmentTreeSum:
    def __init__(self, arr=None):
        if arr:
            self.build(arr)

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
                self.data[curr] = x
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


T = int(input())
for t in range(1, T + 1):
    N, Q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    s = [(-1) ** i * a for i, a in enumerate(arr)]
    ms = [(-1) ** i * a * (i+1) for i, a in enumerate(arr)]
    st_s = SegmentTreeSum(s)
    st_ms = SegmentTreeSum(ms)
    ret = 0
    for _ in range(Q):
        line = input().split()
        op, l, r = line[0], int(line[1]), int(line[2])
        sign = (-1) ** (l-1)
        if op == 'Q':
            q = sign * (st_ms.query(l-1, r-1) -
                        (l-1) * st_s.query(l-1, r-1))
            ret += int(q)
        elif op == 'U':
            st_s.update(l-1, sign * r)
            st_ms.update(l-1, sign * r * l)
    print('Case #{}: {}'.format(t, ret))
