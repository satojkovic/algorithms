def longest_consecutive_bf(nums):
    longest_length = 0
    for num in nums:
        current_num = num
        current_length = 1
        while current_num + 1 in nums:
            current_num += 1
            current_length += 1
        longest_length = max(longest_length, current_length)
    return longest_length


def test_longest_consecutive_bf():
    assert longest_consecutive_bf([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive_bf([0,3,7,2,5,8,4,6,0,1]) == 9
    assert longest_consecutive_bf([1, 1, 1]) == 1


def longest_consecutive(nums):
    nums.sort()
    longest_length = 0
    i = 0
    while i < len(nums):
        j = i + 1
        dup_count = 0
        while j < len(nums):
            if nums[j] - nums[j-1] != 1 and nums[j] - nums[j-1] != 0:
                break
            if nums[j] - nums[j-1] == 0:
                dup_count += 1
            j += 1
        longest_length = max(longest_length, j - i - dup_count)
        i = j
    return longest_length


def test_longest_consecutive():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert longest_consecutive([1, 1, 1]) == 1


def longest_consecutive2(nums):
    if len(nums) == 0:
        return 0
    nums.sort()
    current_length = 1
    longest_length = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            if nums[i] == nums[i-1] + 1:
                current_length += 1
            else:
                longest_length = max(longest_length, current_length)
                current_length = 1
    return max(longest_length, current_length)


def test_longest_consecutive2():
    assert longest_consecutive2([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive2([0,3,7,2,5,8,4,6,0,1]) == 9
    assert longest_consecutive2([1, 1, 1]) == 1


def longest_consecutive_hs(nums):
    nums_set = set(nums)
    longest_length = 0
    for num in nums:
        if num - 1 not in nums_set:
            current_length = 1
            while num + current_length in nums_set:
                current_length += 1
            longest_length = max(longest_length, current_length)
    return longest_length


def test_longest_consecutive_hs():
    assert longest_consecutive_hs([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive_hs([0,3,7,2,5,8,4,6,0,1]) == 9
    assert longest_consecutive_hs([1, 1, 1]) == 1
