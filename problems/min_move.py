def min_move(nums):
    nums = sorted(nums)
    ret = 0
    mid = nums[len(nums) // 2]
    for num in nums:
        ret += abs(num - mid)
    return ret
