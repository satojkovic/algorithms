def find_pivot_idx(nums):
    P = len(nums) * [0]
    for i in range(1, len(nums)):
        P[i] = P[i - 1] + nums[i - 1]
    for i in range(len(nums)):
        left = P[i]
        right = P[-1] - P[i] - nums[i] + nums[-1]
        if left == right:
            return i
    return -1


def test_find_pivot_idx():
    assert find_pivot_idx([1, 7, 3, 6, 5, 6]) == 3
    assert find_pivot_idx([1, 2, 0, 0, 3]) == 2
    assert find_pivot_idx([1]) == 0
    assert find_pivot_idx([]) == -1
