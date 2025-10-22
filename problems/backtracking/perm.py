def permutations(nums):
    if len(nums) == 1:
        return [nums]
    res = []
    for i, n in enumerate(nums):
        former, latter = nums[:i], nums[i + 1 :]
        perms = permutations(former + latter)
        for p in perms:
            res.append(p + [n])
    return res


def perm_backtrack(nums):
    def backtrack(curr):
        if len(curr) == len(nums):
            res.append(curr[:])  # curr[:] means copy values
            return
        for i in range(len(nums)):
            if not seen[i]:
                curr.append(nums[i])
                seen[i] = True
                backtrack(curr)
                seen[i] = False
                curr.pop()

    res = []
    seen = [False] * len(nums)
    backtrack([])
    return res
