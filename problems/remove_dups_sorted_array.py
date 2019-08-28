# Time complexity: O(n)
#  We can iterate over the input array only once.
#
# Space complexity: O(1)
#  We can duplicate values in-place.
#
# Algorithm:
#  Use two pointers. 
#  When the condition nums[j] != nums[i] is True, non-duplicate value is found.
#  Therefore you can insert its value to the position of index (i+1).
def remove_dups1(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums), 1):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1