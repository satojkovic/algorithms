class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res

if __name__ == '__main__':
    S = StockSpanner()
    print(S.next(100))# [(100, 1)] => 1
    print(S.next(80)) # [(100, 1), (80, 1)] => 1
    print(S.next(60)) # [(100, 1), (80, 1), (60, 1)] => 1
    print(S.next(70)) # [(100, 1), (80, 1), (70, 2)] => 2
    print(S.next(60)) # [(100, 1), (80, 1), (70, 2), (60, 1)] => 1
    print(S.next(75)) # [(100, 1), (80, 1), (75, 4)] => 4
    print(S.next(85)) # [(100, 1), (85, 6)] => 6