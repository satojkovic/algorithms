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
        curr = i + self.n - 1
        self.data[curr] = x
        while curr > 0:
            curr = (curr - 1) // 2
            self.data[curr] = min(self.data[2*curr+1], self.data[2*curr+2])


if __name__ == '__main__':
    arr = [5, 3, 7, 9, 1, 4, 6, 2]
    st = SegmentTree()
    st.build(arr)
    print(st.data)
