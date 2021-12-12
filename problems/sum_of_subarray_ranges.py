def subarray_ranges(nums):
    ret = 0
    n = len(nums)
    for i in range(n - 1):
        max_num = nums[i]
        min_num = nums[i]
        for j in range(i + 1, n):
            max_num = max(max_num, nums[j])
            min_num = min(min_num, nums[j])
            ret += max_num - min_num
    return ret


def test_subarray_ranges():
    assert subarray_ranges([1, 2, 3]) == 4
    assert subarray_ranges([4, -2, -3, 4, 1]) == 59
