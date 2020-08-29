def search(nums, target):
    def binary_search(nums, target, head, tail):
        if head > tail:
            return -1
        mid = (head + tail) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > nums[tail]:
            if nums[head] <= target < nums[mid]:
                return binary_search(nums, target, head, mid - 1)
            else:
                return binary_search(nums, target, mid + 1, tail)
        elif nums[mid] < nums[head]:
            if nums[mid] < target <= nums[tail]:
                return binary_search(nums, target, mid + 1, tail)
            else:
                return binary_search(nums, target, head, mid - 1)
        else:
            if nums[mid] > target:
                return binary_search(nums, target, head, mid - 1)
            else:
                return binary_search(nums, target, mid + 1, tail)
    return binary_search(nums, target, 0, len(nums) - 1)

def binary_search(nums, target):
    def _binary_search(nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] < nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                return _binary_search(nums, target, left, mid - 1)
            else:
                return _binary_search(nums, target, mid + 1, right)
        elif nums[mid] < nums[left]:
            if target <= nums[right] and nums[mid] < target:
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

if __name__ == "__main__":
    print(search([11, 18, 25, 4, 5, 6, 7, 10], 18))
    print(search([11, 18, 25, 4, 5, 6, 7, 10], 8))

    print(binary_search([11, 18, 25, 4, 5, 6, 7, 10], 18))
    print(binary_search([11, 18, 25, 4, 5, 6, 7, 10], 8))
