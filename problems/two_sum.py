# Time complexity: O(n)
#  We iterate over the list containing n elements only once.
#  Each lookup in the hash table is O(1)
#
# Space complexity: O(n)
#  The extra space depends on the number of elements in the hash table, which is at most n elements.
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        rest = target - num
        if rest in seen:
            return [seen[rest], i]
        seen[num] = i
    return [-1, -1]


def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]


def two_sum_two_pass(nums, target):
    seen = {}
    for i in range(len(nums)):
        seen[nums[i]] = i
    for i in range(len(nums)):
        rest = target - nums[i]
        if rest in seen and seen[rest] != i:
            return [seen[rest], i]
    return [-1, -1]


def test_two_sum():
    assert two_sum([1, 2, 7, 9], 9) == [1, 2]
    assert two_sum([2, 2, 5, 4], 6) == [1, 3]
    assert two_sum([1, 1, 1, 1, 1], 2) == [0, 1]
    assert two_sum([3, 7, 11], 2) == [-1, -1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([0], 10) == [-1, -1]
