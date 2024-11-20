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
