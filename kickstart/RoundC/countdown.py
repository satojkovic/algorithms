# Test set1: Passed
# Test set2: TLE
def countdown0():
    T = int(input())
    for t in range(1, T + 1):
        N, K = list(map(int, input().split()))
        data = list(map(int, input().split()))
        res = 0
        i = 0
        while i + K <= N:
            if all([True if data[i+j] == K-j else False for j in range(K)]):
                res += 1
                i = i + K
            else:
                i += 1
        print('Case #{}: {}'.format(t, res))

# Test set1: Passed
# Test set2: Passed
def countdown():
    T = int(input())
    for t in range(1, T + 1):
        N, K = list(map(int, input().split()))
        data = list(map(int, input().split()))
        res = 0
        dc = 0
        for i in range(1, N):
            if data[i] == data[i-1] - 1:
                dc += 1
            else:
                dc = 0
            if data[i] == 1 and dc >= K - 1:
                res += 1
        print('Case #{}: {}'.format(t, res))


if __name__ == '__main__':
    countdown()
