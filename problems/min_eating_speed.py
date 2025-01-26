def min_eating_speed_brute_force(piles, h):
    import math
    for k in range(1, 10**9 + 1):
        eating_hours = 0
        for i in range(len(piles)):
            eating_hours += math.ceil(piles[i] / k)
        if eating_hours <= h:
            return k


def test_min_eating_speed_brute_force():
    assert min_eating_speed_brute_force([3,6,7,11], 8) == 4
    assert min_eating_speed_brute_force([30,11,23,4,20], 5) == 30
    assert min_eating_speed_brute_force([30,11,23,4,20], 6) == 23
    assert min_eating_speed_brute_force([10], 1) == 10
    assert min_eating_speed_brute_force([1], 1) == 1
