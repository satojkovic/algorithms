import sys


class SegmentTree:

    def __init__(self, arr=None):
        if arr:
            self.build(arr)

    def build(self, arr):
        self.n = len(arr)
        self.data = [0] * (self.n * 2 - 1)
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
        self.n = len(arr)
        self.data = [0] * (self.n * 2 - 1)
        for i in range(self.n):
            self.data[i + self.n - 1] = arr[i]
        for i in range(self.n - 2, -1, -1):
            self.data[i] = self.data[2*i+1] + self.data[2*i+2]


if __name__ == '__main__':
    arr = [5, 3, 7, 9, 1, 4, 6, 2]
    st = SegmentTree()
    st.build(arr)
    print(st.data)
    print(st.query(1, 5))

    sts = SegmentTreeSum()
    sts.build(arr)
    print(sts.data)
