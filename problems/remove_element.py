def remove_element(nums, val):
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[insert_pos] = nums[i]
            insert_pos += 1
    return insert_pos


def test_remove_element():
    assert remove_element([3, 2, 2, 3], 2) == 2
    assert remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert remove_element([], 4) == 0
    assert remove_element([1], 1) == 0
    assert remove_element([1, 2, 3, 4], 5) == 4


def remove_element_by_swapping_last(nums, val):
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n-1]
            n -= 1
        else:
            i += 1
    return n


def test_remove_element_by_swapping_last():
    assert remove_element_by_swapping_last([3, 2, 2, 3], 2) == 2
    assert remove_element_by_swapping_last([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert remove_element_by_swapping_last([], 4) == 0
    assert remove_element_by_swapping_last([1], 1) == 0
    assert remove_element_by_swapping_last([1, 2, 3, 4], 5) == 4
