import sys
def frog(N, costs):
    dp = [sys.maxsize] * N
    for i in range(N):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = abs(costs[i] - costs[i - 1])
        else:
            dp[i] = min(
                dp[i - 1] + abs(costs[i] - costs[i - 1]),
                dp[i - 2] + abs(costs[i] - costs[i - 2])
            )
    return dp[N - 1]

if __name__ == "__main__":
    print(frog(7, [2, 9, 4, 5, 1, 6, 10]))