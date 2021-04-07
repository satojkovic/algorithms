def record_breaker():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        vs = list(map(int, input().split(' ')))
        prev_max = -1
        res = 0
        for i in range(N):
            if i == N - 1:
                if prev_max < vs[i]:
                    res += 1
                    prev_max = vs[i]
            else:
                if prev_max < vs[i] and vs[i] > vs[i+1]:
                    res +=1
                if prev_max < vs[i]:
                    prev_max = vs[i]
        print('Case #{}: {}'.format(t, res))

if __name__ == '__main__':
    record_breaker()
