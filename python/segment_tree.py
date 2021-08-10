import sys
import math


class SegmentTree:

    def __init__(self, arr=None):
        if arr:
            self.build(arr)

    def build(self, arr):
        self.n = len(arr)
        self.data = [sys.maxsize] * (self.n * 2 - 1)
        # Assign leaf value
        for i in range(self.n):
            self.data[i + self.n - 1] = arr[i]
        # Create parent node
        for i in range(self.n - 2, -1, -1):
            self.data[i] = min(self.data[(2*i)+1], self.data[(2*i)+2])

    def update(self, i, x):
        # Update the leaf node
        curr = i + self.n - 1
        self.data[curr] = x
        # Update parent nodes
        while curr > 0:
            curr = (curr - 1) // 2
            self.data[curr] = min(self.data[2*curr+1], self.data[2*curr+2])

    def query(self, a, b):
        # return min(self.data[a:b])
        def _query(a, b, k, l, r):
            # Outside the segment
            if r <= a or b <= l:
                return sys.maxsize
            # Return the current value because it's in a segment
            if a <= l and r <= b:
                return self.data[k]
            else:
                # Return min(vl, vr) value in the child segment
                vl = _query(a, b, k*2+1, l, (l+r)//2)
                vr = _query(a, b, k*2+2, (l+r)//2, r)
                return min(vl, vr)
        return _query(a, b, 0, 0, self.n)


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
        self.data = [0] * (2 * x - 1)  # Initialize with Identity
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

    # req_l and req_r is an index of an array
    def query(self, req_l, req_r):
        def _query(curr, left, right, req_l, req_r):
            # Out of range
            if req_r < left or right < req_l:
                return 0
            # Matches the range
            if req_l <= left and right <= req_r:
                return self.data[curr]
            # Within range
            mid = (left + right) // 2
            left_sum = _query(2 * curr + 1, left, mid, req_l, req_r)
            right_sum = _query(2 * curr + 2, mid + 1,
                               right, req_l, req_r)
            return left_sum + right_sum

        return _query(0, 0, self.n - 1, req_l, req_r)


if __name__ == '__main__':
    arr = [5, 3, 7, 9, 1, 4, 6, 2]
    st = SegmentTree()
    st.build(arr)
    print(st.data)
    print(st.query(1, 5))

    arr = [1, 3, 5, 7, 9, 11]
    sts = SegmentTreeSum()
    sts.build(arr)
    print(sts.data)

    sts.update(3, 4)
    print(sts.data)
    sts.update(0, -1)
    print(sts.data)

    print(sts.query(2, 5))
    print(sts.query(3, 3))
    print(sts.query(0, 5))
    print(sts.query(1, 2))
