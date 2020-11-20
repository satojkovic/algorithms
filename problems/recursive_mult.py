def recursive_mult(x, y):
    def mult(smaller, larger):
        if smaller == 0:
            return 0
        elif smaller == 1:
            return larger
        s = smaller >> 1
        rets = mult(s, larger)
        retl = rets
        if smaller % 2 != 0:
            retl = mult(smaller - s, larger)
        return rets + retl
    return mult(x, y) if x <= y else mult(y, x)

def recursive_mult2(x, y):
    def mult(smaller, larger, memo):
        if smaller == 0:
            return 0
        elif smaller == 1:
            return larger
        if memo[smaller] > 0:
            return memo[smaller]
        s = smaller >> 1
        rets = mult(s, larger, memo)
        retl = rets
        if smaller % 2 != 0:
            retl = mult(smaller - s, larger, memo)
        memo[smaller] = rets + retl
        return memo[smaller]
    smaller = x if x <= y else y
    larger = x if x <= y else y
    memo = [0 for _ in range(smaller)]
    return mult(smaller, larger, memo)

def recursive_mult3(x, y):
    def mult(smaller, larger, memo):
        if smaller == 0:
            return 0
        elif smaller == 1:
            return larger
        if memo[smaller] > 0:
            return memo[smaller]
        s = smaller >> 1
        rets = mult(s, larger, memo)
        if smaller % 2 == 0:
            memo[smaller] = rets + rets
        else:
            memo[smaller] = rets + rets + larger
        return memo[smaller]
    smaller = x if x <= y else y
    larger = x if x <= y else y
    memo = [0 for _ in range(smaller)]
    return mult(smaller, larger, memo)
