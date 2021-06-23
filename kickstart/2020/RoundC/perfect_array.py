import math


def check_square(x):
    if x >= 0:
        sq = math.sqrt(x)
        return (sq - math.floor(sq)) == 0
    return False


def perfect_array():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))
        res = 0
        for i in range(N):
            for j in range(i, N):
                total = sum(arr[i:j+1])
                if check_square(total):
                    res += 1
        print('Case #{}: {}'.format(t, res))


if __name__ == '__main__':
    perfect_array()
