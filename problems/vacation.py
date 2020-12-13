def vacation(N, scores):
    n_activities = len(scores[0])
    dp = [[0] * n_activities for _ in range(N)]
    for i in range(N):
        dp[i][0] = max(dp[i-1][1] + scores[i][0], dp[i-1][2] + scores[i][0]) \
                    if i != 0 else scores[i][0]
        dp[i][1] = max(dp[i-1][0] + scores[i][1], dp[i-1][2] + scores[i][1]) \
                    if i != 0 else scores[i][1]
        dp[i][2] = max(dp[i-1][0] + scores[i][2], dp[i-1][1] + scores[i][2]) \
                    if i != 0 else scores[i][2]
    return max(dp[N-1][0], dp[N-1][1], dp[N-1][2])

if __name__ == "__main__":
    scores = [[6,7,8], [8,8,3], [2,5,2], [7,8,6], [4,6,8], [2,3,4], [7,5,1]]
    print(vacation(len(scores), scores))
