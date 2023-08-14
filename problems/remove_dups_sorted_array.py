# Time complexity: O(n)
#  We can iterate over the input array only once.
#
# Space complexity: O(1)
#  We can duplicate values in-place.
#
# Algorithm:
#  Use two pointers.
#  When the condition nums[i] != seen is True, non-duplicate value is found.
#  Therefore you can insert its value to the position of index last_insert_pos.
def remove_dups(nums):
    seen = nums[0]
    last_insert_pos = 1
    for i in range(1, len(nums)):
        if nums[i] != seen:
            nums[last_insert_pos] = nums[i]
            last_insert_pos += 1
            seen = nums[i]
    return last_insert_pos


def test_remove_dups():
    assert remove_dups([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
    assert remove_dups([1, 10, 13]) == 3
    assert remove_dups([1, 1, 1, 1, 1]) == 1
    assert remove_dups([-1, -1, 0, 10, 11]) == 4
