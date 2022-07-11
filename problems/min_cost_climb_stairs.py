def min_cost_climb_stairs(cost):
    dp = (len(cost) + 1) * [0]
    for i in range(2, len(cost) + 1):
        dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
    return dp[len(cost)]


def test_min_cost_climb_stairs():
    assert min_cost_climb_stairs([10, 15, 20]) == 15
    assert min_cost_climb_stairs([1, 1, 1, 1, 1]) == 2
    assert min_cost_climb_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
