# Test set1: Passed
# Test set2: TLE
def training():
    import sys
    T = int(input())
    for t in range(1, T + 1):
        N, P = list(map(int, input().split()))
        players = list(map(int, input().split()))
        players = sorted(players, reverse=True)
        res = sys.maxsize
        i = 0
        while i + P - 1 < N:
            max_skill = players[i]
            coaching = sum([max_skill - players[j] for j in range(i + 1, i + P)])
            res = coaching if res > coaching else res
            i += 1
        print('Case #{}: {}'.format(t, res))

if __name__ == '__main__':
    training()
