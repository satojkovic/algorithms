def search(nums, target):
    def _binary_search(nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                return _binary_search(nums, target, left, mid - 1)
            else:
                return _binary_search(nums, target, mid + 1, right)
        elif nums[mid] < nums[left]:
            if nums[mid] < target <= nums[right]:
                return _binary_search(nums, target, mid + 1, right)
            else:
                return _binary_search(nums, target, left, mid - 1)
        else:
            if nums[mid] != nums[right]:
                return _binary_search(nums, target, mid + 1, right)
            else:
                ret = _binary_search(nums, target, left, mid - 1)
                if ret == -1:
                    return _binary_search(nums, target, mid + 1, right)
                else:
                    return ret
    return _binary_search(nums, target, 0, len(nums) - 1)


def test_search():
    assert search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5) == 8
    assert search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 16) == 1
    assert search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 15) == 0
    assert search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 14) == 11
    assert search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 23) == -1
    assert search([2, 2, 2, 3, 4, 2], 4) == 4
