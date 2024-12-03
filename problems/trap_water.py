def trap_bf(height):
    amount = 0
    for i in range(1, len(height) - 1):
        left_max = 0
        right_max = 0
        for j in range(i, -1, -1):
            left_max = max(left_max, height[j])
        for j in range(i, len(height)):
            right_max = max(right_max, height[j])
        amount += min(left_max, right_max) - height[i]
    return amount


def trap_bf2(height):
    amount = 0
    left_max = [height[0]] * len(height)
    right_max = [height[-1]] * len(height)

    for i in range(1, len(height)):
        left_max[i] = max(left_max[i-1], height[i])
    for i in range(len(height) - 2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    for i in range(1, len(height) - 1):
        amount += min(left_max[i], right_max[i]) - height[i]
    return amount


def test_trap_bf():
    assert trap_bf([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap_bf([4,2,0,3,2,5]) == 9
    assert trap_bf([1, 0, 2]) == 1
    assert trap_bf([4, 1, 2]) == 1
    assert trap_bf([1]) == 0
    assert trap_bf([1, 1, 1, 1]) == 0


def test_trap_bf2():
    assert trap_bf2([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap_bf2([4,2,0,3,2,5]) == 9
    assert trap_bf2([1, 0, 2]) == 1
    assert trap_bf2([4, 1, 2]) == 1
    assert trap_bf2([1]) == 0
    assert trap_bf2([1, 1, 1, 1]) == 0
