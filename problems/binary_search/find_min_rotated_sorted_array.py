def find_min(nums):
    if len(nums) == 1 or nums[0] < nums[-1]:
        return nums[0]

    # If the array is rotated, there must be a breakpoint somewhere in the array, so an index out of range will not occur.
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        elif nums[mid - 1] > nums[mid]:
            return nums[mid]
        elif nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1


def test_find_min():
    assert find_min([3,4,5,1,2]) == 1
    assert find_min([4,5,6,7,0,1,2]) == 0
    assert find_min([11,13,15,17]) == 11
    assert find_min([10]) == 10
    assert find_min([1,2,3]) == 1