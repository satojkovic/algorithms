def remove_element(nums, val):
    i, j = 0, 0
    while i < len(nums):
        if nums[i] == val:
            i += 1
            continue
        else:
            nums[j] = nums[i]
            j += 1
            i += 1
    return j


def test_remove_element():
    assert remove_element([3, 2, 2, 3], 2) == 2
    assert remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert remove_element([], 4) == 0
    assert remove_element([1], 1) == 0
    assert remove_element([1, 2, 3, 4], 5) == 4
