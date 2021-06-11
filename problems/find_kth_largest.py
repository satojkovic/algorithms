def find_kth_largest(nums, k):
    return sorted(nums)[-k]


def find_kth_largest1(nums, k):
    import heapq
    return heapq.nlargest(k, nums)[-1]


def test_find_kth_largest():
    assert find_kth_largest([4, 7, 1], 3) == 1
    assert find_kth_largest1([4, 7, 1], 3) == 1

    assert find_kth_largest([3, 2, 1, 3], 3) == 2
    assert find_kth_largest1([3, 2, 1, 3], 3) == 2

    assert find_kth_largest([10], 1) == 10
    assert find_kth_largest1([10], 1) == 10
