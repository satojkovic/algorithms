class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.q = self.k * [0]
        # Not necessarily to have a tail pointer because it can be calculated from head and count variables.
        self.head = 0
        self.count = 0

    def enqueue(self, value):
        if self.is_full():
            return False
        self.q[(self.head + self.count) % self.k] = value
        self.count += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return False
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True

    def front(self):
        if self.is_empty():
            return -1
        return self.q[self.head]

    def rear(self):
        if self.is_empty():
            return -1
        return self.q[(self.head + self.count - 1) % self.k]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.k
