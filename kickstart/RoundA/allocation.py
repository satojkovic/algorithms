def allocation():
    T = int(input())
    for x in range(1, T + 1):
        N, B = list(map(int, input().split()))
        A = list(map(int, input().split()))
        A = sorted(A)
        res, sum = 0, 0
        for a in A:
            sum += a
            if sum > B:
                break
            res += 1
        print('Case #{}: {}'.format(x, res))

if __name__ == '__main__':
    allocation()
