# Time complexity: O(n^2) (need to shift n-1 elems)
# Space complexity: O(1)
def move_zeros1(nums):
    for i in range(len(nums)-1, -1, -1):
        if nums[i] != 0:
            continue
        else:
            tail = nums[-1]
            nums[-1] = nums[i]
            for j in range(len(nums)-2, i, -1):
                tmp = nums[j]
                nums[j] = tail
                tail = tmp
            nums[i] = tail
    return nums

# Time complexity: O(n) (append is O(1) at average case)
# Space complexity: O(n) (non_zeros)
def move_zeros2(nums):
    # count all zeros
    all_zeros = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            all_zeros += 1

    # create non-zero list
    res = []
    for i in range(len(nums)):
        if nums[i] != 0:
            res.append(nums[i])

    # append zeros at tail
    for i in range(all_zeros):
        res.append(0)

    return res

# Time complexity: O(n) (not optimal in case of the array which has all leading zeros[0, 0, ..., 1])
# Space complexity: O(1)
def move_zeros3(nums):
    # Two pointer approach(i and last_non_zero_found_at)
    # Insert just after the last non zero element(where last_non_zero_found_at points)
    last_non_zero_found_at = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_found_at] = nums[i]
            last_non_zero_found_at += 1

    for i in range(last_non_zero_found_at, len(nums), 1):
        nums[i] = 0

    return nums

# Time complexity: O(n)
# Space complexity: O(1)
def move_zeros4(nums):
    last_non_zero_found_at = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[last_non_zero_found_at] = nums[last_non_zero_found_at], nums[i]
            last_non_zero_found_at += 1
    return nums