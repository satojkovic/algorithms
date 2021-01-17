def knapsack(items, max_weight):
    N, W = len(items), max_weight
    dp = [[0] * (W+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for w in range(W+1):
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - items[i-1][0]] + items[i-1][1]) \
                if w - items[i-1][0] >= 0 else dp[i-1][w]
    return dp[N][W]

if __name__ == "__main__":
    items = [(3, 2), (4, 3), (1, 2), (2, 3), (3, 6)]
    print(knapsack(items, max_weight=10))