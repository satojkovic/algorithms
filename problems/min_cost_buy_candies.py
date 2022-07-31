def min_cost_buy_candies(cost):
    cost = sorted(cost, reverse=True)
    return sum(cost) - sum(cost[2::3])


def test_min_cost_buy_candies():
    assert min_cost_buy_candies([1]) == 1
    assert min_cost_buy_candies([1, 2]) == 3
    assert min_cost_buy_candies([3, 4, 10]) == 14
    assert min_cost_buy_candies([1, 1, 1, 1, 1]) == 4
