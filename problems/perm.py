def perm1(nums):
    if len(nums) < 2:
        return [nums]
    ret = []
    for i, num in enumerate(nums):
        pivot = num
        perm = perm1(nums[:i] + nums[i+1:])
        ret += [[pivot] + p for p in perm]
    return ret

def perm2(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        # type(s): list
        return [s]
    ret = []
    for i, ch in enumerate(s):
        res = perm2(s[:i] + s[i+1:])
        ret.extend([[ch] + r for r in res])
    return ret