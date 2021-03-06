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

def max_subarray3(nums):
    def _get_left_right_sum(nums, left, right, mid):
        left_sum = float('-inf')
        curr_sum = 0
        for i in range(mid, left - 1, -1):
            curr_sum += nums[i]
            left_sum = max(curr_sum, left_sum)

        right_sum = float('-inf')
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            right_sum = max(curr_sum, right_sum)

        return left_sum + right_sum

    def _get_max_subarray(nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        left_sum = _get_max_subarray(nums, left, mid)
        right_sum = _get_max_subarray(nums, mid + 1, right)
        left_right_sum = _get_left_right_sum(nums, left, right, mid)
        return max(left_sum, right_sum, left_right_sum)

    return _get_max_subarray(nums, 0, len(nums) - 1) if len(nums) != 0 else None