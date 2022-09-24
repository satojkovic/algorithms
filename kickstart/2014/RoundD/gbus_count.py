T = int(input())
for t in range(1, T + 1):
    if t != 1:
        _ = input()
    N = int(input())
    city_ranges = list(map(int, input().split()))
    segments = [[city_ranges[i], city_ranges[i+1]]
                for i in range(0, len(city_ranges), 2)]
    P = int(input())
    res = []
    for _ in range(P):
        c = int(input())
        ans = 0
        for i in range(N):
            if segments[i][0] <= c <= segments[i][1]:
                ans += 1
        res.append(str(ans))
    print('Case #{}: {}'.format(t, ' '.join(res)))
