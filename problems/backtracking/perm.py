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


def test_perm_backtrack():
    assert perm_backtrack([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]

    assert perm_backtrack([1, 2, 3]) == [[1, 2, 3],
                                        [1, 3, 2],
                                        [2, 1, 3],
                                        [2, 3, 1],
                                        [3, 1, 2],
                                        [3, 2, 1]]
    assert perm_backtrack([0, 1]) == [[0, 1], [1, 0]]
    assert perm_backtrack([1]) == [[1]]
