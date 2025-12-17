from typing import List

def findTargetSumWays(nums: List[int], target: int) -> int:
    def backtrack(index, current_sum):
        if (index, current_sum) in memo:
            return memo[(index, current_sum)]

        if index == len(nums):
            return 1 if current_sum == target else 0

        count_plus = backtrack(index + 1, current_sum + nums[index])
        count_minus = backtrack(index + 1, current_sum - nums[index])

        memo[(index, current_sum)] = count_plus + count_minus

        return memo[(index, current_sum)]

    memo = {}
    return backtrack(0, 0)


def test_target_sum():
    assert findTargetSumWays([1,1,1,1,1], 3) == 5
    assert findTargetSumWays([1], 1) == 1

