# Time complexity: O(n)
#  We can iterate over the input array only once.
#
# Space complexity: O(1)
#  We can duplicate values in-place.
#
# Algorithm:
#  Use two pointers.
#  When the condition nums[k] != nums[i] is True, non-duplicate value is found.
#  Therefore you can insert its value to the position of index (k+1).
def remove_dups(nums):
    if len(nums) == 0:
        return 0
    k = 0
    for i in range(1, len(nums)):
        if nums[k] != nums[i]:
            k += 1
            nums[k] = nums[i]
    return k + 1


def test_remove_dups():
    assert remove_dups([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
    assert remove_dups([]) == 0
    assert remove_dups([1, 10, 13]) == 3
    assert remove_dups([1, 1, 1, 1, 1]) == 1
    assert remove_dups([-1, -1, 0, 10, 11]) == 4
