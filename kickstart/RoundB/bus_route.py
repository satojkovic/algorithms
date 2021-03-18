from itertools import product

def check(days):
    for i in range(len(days)-1):
        if days[i] > days[i + 1]:
            return False
    return True

# Samples: Passed
# Test set1: TLE
# Test set2: Skipped
def bus_route():
    T = int(input())
    for t in range(1, T + 1):
        N, D = list(map(int, input().split()))
        Xs = list(map(int, input().split()))
        n_days = []
        for X in Xs:
            day = X
            days = []
            while day <= D:
                days.append(day)
                day += X
            n_days.append(days)
        res = n_days[0][0]
        for days in product(*n_days):
            if check(days):
                res = days[0] if days[0] > res else res
        print('Case #{}: {}'.format(t, res))

# Test set1: Passed
# Test set2: TLE
def bus_route2():
    import math
    T = int(input())
    for t in range(1, T + 1):
        N, D = list(map(int, input().split()))
        Xs = list(map(int, input().split()))
        for k in range(D, 0, -1):
            days = [math.ceil(k / Xs[0]) * Xs[0]]
            for i in range(1, N):
                days.append(math.ceil(days[i-1] / Xs[i]) * Xs[i])
            if days[-1] <= D:
                print('Case #{}: {}'.format(t, days[0]))
                break

if __name__ == '__main__':
    bus_route2()
