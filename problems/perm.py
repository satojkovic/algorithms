def perm1(nums):
    if len(nums) < 2:
        return [nums]
    ret = []
    for i, num in enumerate(nums):
        pivot = num
        perm = perm1(nums[:i] + nums[i+1:])
        ret += [[pivot] + p for p in perm]
    return ret
