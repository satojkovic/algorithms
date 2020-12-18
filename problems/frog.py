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

if __name__ == "__main__":
    print(frog(7, [2, 9, 4, 5, 1, 6, 10]))
    print(frog2(7, [2, 9, 4, 5, 1, 6, 10]))
