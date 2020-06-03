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

if __name__ == "__main__":
    print(search([11, 18, 25, 4, 5, 6, 7, 10], 18))
    print(search([11, 18, 25, 4, 5, 6, 7, 10], 8))