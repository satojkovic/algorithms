def perfect_array():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))
        cumsum = [arr[0] if i == 0 else 0 for i in range(N)]
        for i in range(1, N):
            cumsum[i] = cumsum[i - 1] + arr[i]
        res = 0
        for i in range(N):
            for j in range(i, N):
                total = cumsum[j] - cumsum[i - 1] if i != 0 else cumsum[j]
                if total == 0:
                    res += 1
                k = 1
                while k**2 <= total:
                    if total // k == k and total % k == 0:
                        res += 1
                        break
                    k += 1
        print('Case #{}: {}'.format(t, res))


if __name__ == '__main__':
    perfect_array()
