def merge_two_sorted_array_(nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()


def merge_two_sorted_array(nums1, m, nums2, n):
    # merge arrays backwards
    merged_idx = m + n - 1
    idx_m, idx_n = m - 1, n - 1
    while idx_n >= 0:
        if idx_m >= 0 and nums1[idx_m] >= nums2[idx_n]:
            nums1[merged_idx] = nums1[idx_m]
            idx_m -= 1
        else:
            nums1[merged_idx] = nums2[idx_n]
            idx_n -= 1
        merged_idx -= 1


def test_merge_two_sorted_array():
    a = [1, 2, 3, 0, 0, 0]
    b = [2, 5, 6]
    merge_two_sorted_array(a, b, 3, 3)
    assert a == [1, 2, 2, 3, 5, 6]

    a = [1, 3, 7, 8, 0, 0, 0]
    b = [2, 4, 11]
    merge_two_sorted_array(a, b, 4, 3)
    assert a == [1, 2, 3, 4, 7, 8, 11]

    a = [2, 5, 0, 0, 0, 0]
    b = [1, 6, 7, 8]
    merge_two_sorted_array(a, b, 2, 4)
    assert a == [1, 2, 5, 6, 7, 8]

    a = [1]
    b = []
    merge_two_sorted_array(a, b, 1, 0)
    assert a == [1]

    a = [0]
    b = [1]
    merge_two_sorted_array(a, b, 0, 1)
    assert a == [1]
