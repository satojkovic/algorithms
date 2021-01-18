def knapsack(items, max_weight):
    N, W = len(items), max_weight
    dp = [[0] * (W+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for w in range(W+1):
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - items[i-1][0]] + items[i-1][1]) \
                if w - items[i-1][0] >= 0 else dp[i-1][w]
    return dp[N][W]

def edit_distance(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    dp[0] = [c for c in range(len(t) + 1)]
    for r in range(1, len(s) + 1):
        dp[r][0] = dp[r-1][0] + 1
    for r in range(1, len(s) + 1):
        for c in range(1, len(t) + 1):
            if s[r-1] == t[c-1]:
                dp[r][c] = min(dp[r-1][c-1], dp[r-1][c] + 1, dp[r][c-1] + 1)
            else:
                dp[r][c] = min(dp[r-1][c-1] + 1, dp[r-1][c] + 1, dp[r][c-1] + 1)
    return dp[len(s)][len(t)]

if __name__ == "__main__":
    items = [(3, 2), (4, 3), (1, 2), (2, 3), (3, 6)]
    print(knapsack(items, max_weight=10))

    print(edit_distance('saka', 'ana'))
    print(edit_distance('logistic', 'algorithm'))