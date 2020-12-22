import sys
def frog(N, costs):
    dp = [sys.maxsize] * N
    dp[0] = 0
    for i in range(1, N):
        if i == 1:
            dp[i] = abs(costs[i] - costs[i - 1])
        else:
            dp[i] = min(
                dp[i - 1] + abs(costs[i] - costs[i - 1]),
                dp[i - 2] + abs(costs[i] - costs[i - 2])
            )
    return dp[N - 1]

def frog2(N, costs):
    def chmin(a, b):
        return b if a > b else a
    dp = [sys.maxsize] * N
    dp[0] = 0
    for i in range(1, N):
        dp[i] = chmin(dp[i], dp[i - 1] + abs(costs[i] - costs[i - 1]))
        if i > 1:
            dp[i] = chmin(dp[i], dp[i - 2] + abs(costs[i] - costs[i - 2]))
    return dp[N - 1]

def frog3(N, costs):
    def chmin(a, b):
        return b if a > b else a
    dp = [sys.maxsize] * N
    dp[0] = 0
    for i in range(N):
        if i + 1 < N:
            dp[i + 1] = chmin(dp[i + 1], dp[i] + abs(costs[i] - costs[i + 1]))
        if i + 2 < N:
            dp[i + 2] = chmin(dp[i + 2], dp[i] + abs(costs[i] - costs[i + 2]))
    return dp[N - 1]

def frog4(N, costs):
    def frog_r(pos, costs):
        if pos == 0:
            return 0
        res = sys.maxsize
        res = min(res, frog_r(pos-1, costs) + abs(costs[pos] - costs[pos-1]))
        if pos > 1:
            res = min(res, frog_r(pos-2, costs) + abs(costs[pos] - costs[pos-2]))
        return res
    return frog_r(N-1, costs)

def frog5(N, costs):
    def frog_r(pos, costs, memo):
        if pos == 0:
            return 0
        if memo[pos] < sys.maxsize:
            return memo[pos]
        res = sys.maxsize
        res = min(res, frog_r(pos-1, costs, memo) + abs(costs[pos] - costs[pos-1]))
        if pos > 1:
            res = min(res, frog_r(pos-2, costs, memo) + abs(costs[pos] - costs[pos-2]))
        memo[pos] = res
        return res
    memo = [sys.maxsize] * N
    return frog_r(N-1, costs, memo)

if __name__ == "__main__":
    print(frog(7, [2, 9, 4, 5, 1, 6, 10]))
    print(frog2(7, [2, 9, 4, 5, 1, 6, 10]))
    print(frog3(7, [2, 9, 4, 5, 1, 6, 10]))
    print(frog4(7, [2, 9, 4, 5, 1, 6, 10]))
    print(frog5(7, [2, 9, 4, 5, 1, 6, 10]))
