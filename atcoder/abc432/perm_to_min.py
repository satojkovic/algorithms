
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


num = int(input())
nums = [s for s in str(num)]
perm_nums = perm_backtrack(nums)
nonzero_head_nums = [''.join(perm_num) for perm_num in perm_nums if perm_num[0] != '0']
print(min(list(map(int, nonzero_head_nums))))
