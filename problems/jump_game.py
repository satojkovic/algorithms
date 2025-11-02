from typing import List

# Time complexity: O(n^2) in the worst case
# Space complexity: O(N)
def canJump_backtrack(self, nums: List[int]) -> bool:
    def backtrack(index):
        if index == len(nums) - 1:
            return "Good"
        if index >= len(nums):
            return "Bad"

        if memo[index] != "UNKNOWN":
            return memo[index]

        for jump in range(1, nums[index] + 1):
            if backtrack(index + jump) == "Good":
                memo[index] = "Good"
                return memo[index]

        memo[index] = "Bad"
        return memo[index]

    memo = ["UNKNOWN"] * len(nums)
    res = backtrack(0)
    return True if res == "Good" else False

def canJump_greedy(nums: List[int]) -> bool:
    reach = 0
    for i in range(len(nums)):
        if i > reach:
            return False
        reach = max(reach, i + nums[i])
        if reach >= len(nums) - 1:
            return True
    return True

def test_canJump_backtrack():
    assert canJump_backtrack(None, [2, 3, 1, 1, 4]) is True
    assert canJump_backtrack(None, [3, 2, 1, 0, 4]) is False


def test_canJump_greedy():
    assert canJump_greedy([2, 3, 1, 1, 4]) is True
    assert canJump_greedy([3, 2, 1, 0, 4]) is False