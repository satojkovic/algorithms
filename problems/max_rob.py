def max_rob(nums):
    N = len(nums)
    dp = (N + 1) * [0]
    dp[1] = nums[0]
    for i in range(2, N + 1):
        dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
    return dp[-1]


def max_rob_space_optim(nums):
    N = len(nums)
    dp = [0, nums[0]]
    for i in range(2, N + 1):
        curr = max(dp[0] + nums[i-1], dp[1])
        dp[0], dp[1] = dp[1], curr
    return dp[1]


def max_rob_recursion_with_memo(nums):
    def rob_from(i, nums, memo):
        if i >= len(nums):
            return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = max(rob_from(i+1, nums, memo),
                      rob_from(i+2, nums, memo) + nums[i])
        return memo[i]

    memo = len(nums) * [-1]
    return rob_from(0, nums, memo)


def test_max_rob():
    assert max_rob([2, 7, 9, 3, 1]) == 12
    assert max_rob([1, 2, 3, 1]) == 4
    assert max_rob([10]) == 10
    assert max_rob([0, 0, 100]) == 100

    assert max_rob_space_optim([2, 7, 9, 3, 1]) == 12
    assert max_rob_space_optim([1, 2, 3, 1]) == 4
    assert max_rob_space_optim([10]) == 10
    assert max_rob_space_optim([0, 0, 100]) == 100


def test_max_rob_recursion_with_memo():
    assert max_rob_recursion_with_memo([2, 7, 9, 3, 1]) == 12
    assert max_rob_recursion_with_memo([1, 2, 3, 1]) == 4
    assert max_rob_recursion_with_memo([10]) == 10
    assert max_rob_recursion_with_memo([0, 0, 100]) == 100
