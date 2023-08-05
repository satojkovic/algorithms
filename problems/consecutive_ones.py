def max_consecutive_ones(nums):
    max_len, count = 0, 0
    for i in range(len(nums)):
        if nums[i] == 0:
            max_len = max(max_len, count)
            count = 0
        else:
            count += 1
    return max(max_len, count)


def test_max_consecutive_ones():
    assert max_consecutive_ones([1, 0, 1, 0, 1, 1, 0]) == 2
    assert max_consecutive_ones([1, 1, 1]) == 3
    assert max_consecutive_ones([0, 0, 0, 0]) == 0
