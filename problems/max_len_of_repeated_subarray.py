def find_length(nums1, nums2):
    def check(length):
        seen = set(tuple(nums1[i:i+length])
                   for i in range(len(nums1) - length + 1))
        return any(tuple(nums2[j:j+length]) in seen for j in range(len(nums2) - length + 1))
    left, right = 0, min(len(nums1), len(nums2)) + 1
    while right - left > 1:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid
        else:
            right = mid
    return left


def test_find_length():
    assert find_length([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3
    assert find_length([0, 0, 0], [0, 0]) == 2
    assert find_length([1, 2], [2, 3, 1, 2]) == 2
    assert find_length([1, 3, 5], [5, 4, 2]) == 1
    assert find_length([10], [20]) == 0
    assert find_length([1, 2, 3], [4, 5, 6, 7, 8]) == 0
