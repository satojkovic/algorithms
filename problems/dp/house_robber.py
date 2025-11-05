from typing import List

def rob(nums: List[int]) -> int:
    def rob_recursive(index):
        if index >= N:
            return 0
        if memo[index] != -1:
            return memo[index]
        memo[index] = max(nums[index] + rob_recursive(index + 2), rob_recursive(index + 1))
        return memo[index]

    N = len(nums)
    memo = [-1] * N
    return rob_recursive(0)


def test_rob():
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([2, 1, 1, 2]) == 4
    assert rob([0]) == 0
    assert rob([1]) == 1
    assert rob([1, 2]) == 2
    assert rob([2, 1]) == 2
    assert rob([10, 1, 1, 10]) == 20
    assert rob([0, 0, 0, 0]) == 0
    assert rob([5, 5, 5, 5, 5]) == 15
