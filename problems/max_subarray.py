# Time complexity: O(n^3)
#  For every start index i and end index, calculate the sum of its subarray
#
# Space complexity: O(1)
#  No extra space is allocated.
#
# Algorithm:
#  Check all subarray
def max_subarray1(nums):
    ret = nums[0] if len(nums) != 0 else None
    for i in range(0, len(nums) - 1, 1):
        for j in range(len(nums) - 1, 0, -1):
            if sum(nums[i:j+1]) > ret:
                ret = sum(nums[i:j+1])
    return ret

# Time complexity: O(n)
#  We iterate over entire array only once.
#
# Space complexity: O(1)
#  Only a fixed number of variables are needed.
# 
# Algorithm:
#  When the element of index i is greater than the sum of previous subarray, the local max is re-initialized by the element of index i.
#  When the local max is greater thatn the global max, the global max is replaced by the local max.
def max_subarray2(nums):
    n = len(nums)
    if len(nums) == 0:
        return None
    local_max = nums[0]
    global_max = nums[0]
    for i in range(1, n):
        local_max = max(nums[i], local_max + nums[i])
        global_max = max(local_max, global_max)
    return global_max