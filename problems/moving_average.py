class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.q = []
        self.prev_sum = 0

    def next(self, val):
        if len(self.q) == self.size:
            self.prev_sum -= self.q.pop(0)
        self.prev_sum += val
        self.q.append(val)
        return self.prev_sum / len(self.q)