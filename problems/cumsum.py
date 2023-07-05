def cumsum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]
    return nums


def test_cumsum():
    nums = [1, 2, 3, 4, 5]
    assert cumsum(nums) == [1, 3, 6, 10, 15]

    nums = [1, -2, 3, -4, -5]
    assert cumsum(nums) == [1, -1, 2, -2, -7]

    nums = [10]
    assert cumsum(nums) == [10]
