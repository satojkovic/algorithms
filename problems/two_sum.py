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


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
