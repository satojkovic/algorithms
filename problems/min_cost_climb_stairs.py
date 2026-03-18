def min_cost_climb_stairs(cost):
    num_costs = len(cost)
    min_cost = (num_costs + 1) * [0]
    for i in range(2, num_costs + 1):
        min_cost[i] = min(min_cost[i-2] + cost[i-2], min_cost[i-1] + cost[i-1])
    return min_cost[num_costs]


def test_min_cost_climb_stairs():
    assert min_cost_climb_stairs([10, 15, 20]) == 15
    assert min_cost_climb_stairs([1, 1, 1, 1, 1]) == 2
    assert min_cost_climb_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
