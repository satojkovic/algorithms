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
    print(S.next(100))
    print(S.next(80))
    print(S.next(60))
    print(S.next(70))
    print(S.next(60))
    print(S.next(75))
    print(S.next(85))