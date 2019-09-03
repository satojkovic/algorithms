def prod_except_self1(nums):
    L = len(nums) * [1]
    R = len(nums) * [1]
    for i in range(1, len(nums)):
        L[i] = nums[i-1] * L[i-1]
    for i in reversed(range(len(nums) - 1)):
        R[i] = nums[i+1] * R[i+1]
    return [L[i] * R[i] for i in range(len(nums))]