def wiggle_sort(nums):
    nums = sorted(nums)
    i = 1
    while i <= len(nums) - 2:
        nums[i], nums[i+1] = nums[i+1], nums[i]
        i += 2
    return nums


def test_wiggle_sort():
    assert wiggle_sort([3, 5, 2, 1, 6, 4]) == [1, 3, 2, 5, 4, 6]
    assert wiggle_sort([1]) == [1]
    assert wiggle_sort([10, 3, 4]) == [3, 10, 4]
