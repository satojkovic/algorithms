T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ret = 0
    for i in range(N):
        for j in range(i, N):
            s = sum(arr[i:j+1])
            if s < 0:
                i = j + 1
                break
            ret += s
    print('Case #{}: {}'.format(t, ret))
