import math


def check_square(x):
    if x >= 0:
        sq = math.sqrt(x)
        return (sq - math.floor(sq)) == 0
    return False


def cumulative_sum(arr):
    N = len(arr)
    cum_sum = [0] * (N+1)
    for i in range(N):
        cum_sum[i+1] = cum_sum[i] + arr[i]
    return cum_sum


def perfect_array():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))
        cum_sum = cumulative_sum(arr)
        res = 0
        for i in range(N):
            for j in range(i, N):
                total = cum_sum[j+1] - cum_sum[i]
                if check_square(total):
                    res += 1
        print('Case #{}: {}'.format(t, res))


def perfect_array2():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))
        res = 0
        curr_sum, min_sum = 0, 0
        m = {0: 1}
        for i in range(N):
            curr_sum += arr[i]
            min_sum = min(min_sum, curr_sum)
            j = 0
            while curr_sum - (j * j) >= min_sum:
                if curr_sum - (j * j) in m:
                    res += m[curr_sum - j*j]
                j += 1
            if curr_sum in m:
                m[curr_sum] += 1
            else:
                m[curr_sum] = 1
        print('Case #{}: {}'.format(t, res))


def test_cumulative_sum():
    assert cumulative_sum([1, 2, 3, 4, 5]) == [0, 1, 3, 6, 10, 15]


if __name__ == '__main__':
    perfect_array2()
