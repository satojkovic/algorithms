def search_range(nums, target):
    if len(nums) == 0:
        return [-1, -1]
    lb, ub = lower_bound(nums, target), upper_bound(nums, target)
    return [lb, ub]


def lower_bound(nums, target):
    left, right = -1, len(nums) - 1
    while right - left > 1:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid
    return right if nums[right] == target else -1


def upper_bound(nums, target):
    left, right = 0, len(nums)
    while right - left > 1:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid
    return left if nums[left] == target else -1


def test_search_range():
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert search_range([], 0) == [-1, -1]
    assert search_range([0], 0) == [0, 0]
