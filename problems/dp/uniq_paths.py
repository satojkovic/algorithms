def uniquePaths(m: int, n: int) -> int:
    dp = [[0] * n for _ in range(m)]
    for col in range(n):
        dp[0][col] = 1
    for row in range(m):
        dp[row][0] = 1

    for row in range(1, m):
        for col in range(1, n):
            dp[row][col] = dp[row-1][col] + dp[row][col-1]

    return dp[m-1][n-1]


def test_uniquePaths():
    assert uniquePaths(3, 7) == 28
    assert uniquePaths(3, 2) == 3
    assert uniquePaths(1, 1) == 1
    assert uniquePaths(1, 5) == 1
    assert uniquePaths(5, 1) == 1
