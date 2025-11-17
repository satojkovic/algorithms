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

nums = input().split()
perm_nums = perm_backtrack(nums)
perm_nums = list(map(int, [''.join(perm_num) for perm_num in perm_nums]))
print(max(perm_nums))
