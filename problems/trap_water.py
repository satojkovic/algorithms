def trap_bf(height):
    total_amount = 0
    # Calculate the amount of water that can be stored at each location
    for i in range(1, len(height) - 1):
        left_max = 0
        right_max = 0
        # Update left_max and right_max by comparison including the value of the current position.
        for j in range(i, -1, -1):
            left_max = max(left_max, height[j])
        for j in range(i, len(height)):
            right_max = max(right_max, height[j])
        total_amount += min(left_max, right_max) - height[i]
    return total_amount


def trap_bf_precompute(height):
    total_amount = 0
    left_max = [height[0]] * len(height)
    right_max = [height[-1]] * len(height)

    # left_max and right_max are pre-calculated
    for i in range(1, len(height)):
        left_max[i] = max(left_max[i-1], height[i])
    for i in range(len(height) - 2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    for i in range(1, len(height) - 1):
        total_amount += min(left_max[i], right_max[i]) - height[i]
    return total_amount



def test_trap_bf():
    assert trap_bf([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap_bf([4,2,0,3,2,5]) == 9
    assert trap_bf([1, 0, 2]) == 1
    assert trap_bf([4, 1, 2]) == 1
    assert trap_bf([1]) == 0
    assert trap_bf([1, 1, 1, 1]) == 0


def test_trap_bf_precompute():
    assert trap_bf_precompute([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap_bf_precompute([4,2,0,3,2,5]) == 9
    assert trap_bf_precompute([1, 0, 2]) == 1
    assert trap_bf_precompute([4, 1, 2]) == 1
    assert trap_bf_precompute([1]) == 0
    assert trap_bf_precompute([1, 1, 1, 1]) == 0
