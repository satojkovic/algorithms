def search_position(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


def test_search_position():
    assert search_position([1, 3, 5, 6], 5) == 2
    assert search_position([1, 3, 5, 6], 2) == 1
    assert search_position([1, 3, 5, 6], 7) == 4
    assert search_position([1, 3, 5, 6], 0) == 0
