# Test set1: Passed
# Test set2: Passed
def bike_tour():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        ckpts = list(map(int, input().split()))
        res = 0
        for i in range(1, N - 1):
            if ckpts[i - 1] < ckpts[i] and ckpts[i] > ckpts[i + 1]:
                res += 1
        print('Case #{}: {}'.format(t, res))


if __name__ == '__main__':
    bike_tour()
