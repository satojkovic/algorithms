def remove_element(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


def test_remove_element():
    assert remove_element([3, 2, 2, 3], 2) == 2
    assert remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert remove_element([], 4) == 0
    assert remove_element([1], 1) == 0
    assert remove_element([1, 2, 3, 4], 5) == 4
