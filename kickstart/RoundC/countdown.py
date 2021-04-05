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
            if all([True if data[i+j]==K-j else False for j in range(K)]):
                res += 1
                i = i + K
            else:
                i += 1
        print('Case #{}: {}'.format(t, res))

def countdown(N, K, data):
    res = 0
    i = N - 1
    while i >= 0:
        if data[i] != 1:
            i -= 1
            continue
        j = i - 1
        up = 1
        while j >= 0:
            if data[i] + up != data[j]:
                break
            up += 1
            j -= 1
        if up >= K:
            res += 1
        i = j
    print('Case #: {}'.format(res))

if __name__ == '__main__':
    countdown0()
