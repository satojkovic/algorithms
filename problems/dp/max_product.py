from typing import List

def maxProduct(nums: List[int]) -> int:
    global_max = nums[0]
    prev_max_so_far = nums[0]
    prev_min_so_far = nums[0]

    for i in range(1, len(nums)):
        curr_num = nums[i]
        curr_max_so_far = max(curr_num, prev_max_so_far * curr_num, prev_min_so_far * curr_num)
        curr_min_so_far = min(curr_num, prev_max_so_far * curr_num, prev_min_so_far * curr_num)
        global_max = max(global_max, curr_max_so_far)
        prev_max_so_far = curr_max_so_far
        prev_min_so_far = curr_min_so_far

    return global_max


def test_maxProduct():
    assert maxProduct([2, 3, -2, 4]) == 6
    assert maxProduct([-2, 0, -1]) == 0
    assert maxProduct([-2, 3, -4]) == 24
    assert maxProduct([-1, -3, -10, 0, 60]) == 60
    assert maxProduct([-2, -3, 0, -2, -40]) == 80
    assert maxProduct([0, 2]) == 2
    assert maxProduct([-2]) == -2
    assert maxProduct([3, -1, 4]) == 4
    assert maxProduct([-1, -2, -9, -6]) == 108
