def combinations(n, k):
    def combi(nums, k):
        if k == 1:
            return [[v] for v in nums]
        if len(nums) == k:
            return [nums]
        ret = []
        for i in range(len(nums) - k + 1):
            res = combi(nums[i+1:], k - 1)
            for r in res:
                ret.append(r + [nums[i]])
        return ret
    nums = [i+1 for i in range(n)]
    return combi(nums, k)


def test_combinations():
    ret = combinations(4, 2)
    assert ret == [[2, 1], [3, 1], [4, 1], [3, 2], [4, 2], [4, 3]]
    ret = combinations(1, 1)
    assert ret == [[1]]
    ret = combinations(4, 3)
    assert ret == [[3, 2, 1], [4, 2, 1], [4, 3, 1], [3, 4, 2]]
    ret = combinations(5, 1)
    assert ret == [[1], [2], [3], [4], [5]]
