def three_sum_bf(nums):
    nums.sort()
    triplets = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if sum([nums[i], nums[j], nums[k]]) == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
    return list(triplets)


def test_three_sum_bf():
    assert three_sum_bf([-1,0,1,2,-1,-4]) == [(-1, 0, 1), (-1, -1, 2)]
    assert not three_sum_bf([0,1,1])
    assert three_sum_bf([0,0,0]) == [(0,0,0)]
