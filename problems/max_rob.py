def max_rob(nums):
    N = len(nums)
    dp = (N + 1) * [0]
    dp[1] = nums[0]
    for i in range(2, N + 1):
        dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
    return dp[-1]


def test_max_rob():
    assert max_rob([2, 7, 9, 3, 1]) == 12
    assert max_rob([1, 2, 3, 1]) == 4
    assert max_rob([10]) == 10
    assert max_rob([0, 0, 100]) == 100
