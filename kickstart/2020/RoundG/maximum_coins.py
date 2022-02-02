T = int(input())
for t in range(1, T+1):
    N = int(input())
    values = []
    for i in range(N):
        values.append(list(map(int, input().split())))
    max_value = -1
    for row in range(N):
        for col in range(N):
            if row > 1 and col > 1:
                break
            val = 0
            for delta in range(N):
                if row + delta >= N or col + delta >= N:
                    break
                val += values[row+delta][col+delta]
            if max_value < val:
                max_value = val
    print('Case #{}: {}'.format(t, max_value))
