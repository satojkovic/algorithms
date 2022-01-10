def min_swaps(nums):
    n = sum(nums)
    circular_nums = nums + nums
    one_in_window = 0
    max_one_in_window = 0
    # +1 if nums[i] == 1 else 0
    # but when i is greater than window size `n`, -1 first if nums[i - n] == 1
    for i in range(len(circular_nums)):
        if i >= n and circular_nums[i - n] == 1:
            one_in_window -= 1
        if circular_nums[i] == 1:
            one_in_window += 1
        max_one_in_window = max(max_one_in_window, one_in_window)
    return n - max_one_in_window


def test_min_swaps():
    assert min_swaps([0, 1, 0, 1, 1, 0, 0]) == 1
    assert min_swaps([1]) == 0
    assert min_swaps([1, 0, 1, 1]) == 0
    assert min_swaps([0, 1, 1, 1, 0, 0, 1, 1, 0]) == 2
