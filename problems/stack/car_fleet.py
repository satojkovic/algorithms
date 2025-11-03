def car_fleet(target, position, speed):
    pair = [[p, s] for p, s in zip(position, speed)]
    stack = []
    for p, s in sorted(pair)[::-1]:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-2] >= stack[-1]:
            stack.pop()
    return len(stack)


def test_car_fleet():
    assert car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
    assert car_fleet(10, [3], [3]) == 1
    assert car_fleet(100, [0, 2, 4], [4, 2, 1]) == 1
