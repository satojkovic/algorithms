def find_median(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
    else:
        return merged[n // 2]

def test_find_median():
    assert find_median([1, 3], [2]) == 2.0
    assert find_median([1, 2], [3, 4]) == 2.5
    assert find_median([], [3]) == 3.0
    assert find_median([1], []) == 1.0
