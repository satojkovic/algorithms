def solution(N, Ws, Ps):
    def backtrack(n, current):
        if tuple(current) in memo:
            return
        if n == N:
            if current[1] <= current[2]:
                res.append(current)
            return
        backtrack(n + 1, list(map(lambda x, y: x + y, current, [1, Ws[n], 0])))
        backtrack(n + 1, list(map(lambda x, y: x + y, current, [0, 0, Ps[n]])))
        memo[tuple(current)] = res

    memo = {}
    res = []
    current = [0, 0, 0] # [num_of_dogs, sum_of_w, sum_of_p]
    backtrack(0, current)
    ans_idx = 0
    for i in range(len(res)):
        if res[i][0] > res[ans_idx][0]:
            ans_idx = i
    return res[ans_idx][0]

T = int(input())
for t in range(T):
    N = int(input())
    Ws, Ps = [], []
    for n in range(N):
        W, P = list(map(int, input().split()))
        Ws.append(W)
        Ps.append(P)
    ans = solution(N, Ws, Ps)
    print(ans)
