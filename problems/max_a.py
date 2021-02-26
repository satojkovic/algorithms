def max_a(N):
    dp = [[0] * (N+1) for _ in range(3)]
    buf = [[0] * (N+1) for _ in range(2)]
    for i in range(1, N + 1):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1]) + 1
        res_s2 = dp[1][i-1] + buf[0][i-1]
        res_s3 = dp[2][i-1] + buf[1][i-1]
        if res_s2 <= res_s3:
            dp[1][i] = res_s3
            buf[0][i] = buf[1][i-1]
        else:
            dp[1][i] = res_s2
            buf[0][i] = buf[0][i-1]
        if i >= 3:
            buf[1][i] = max(dp[0][i-3], dp[1][i-3], dp[2][i-3])
            dp[2][i] = buf[1][i] * 2
    return max(dp[0][N], dp[1][N], dp[2][N])    

if __name__ == '__main__':
    print(max_a(7)) # => 9
