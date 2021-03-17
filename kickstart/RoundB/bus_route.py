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

if __name__ == '__main__':
    bus_route()
