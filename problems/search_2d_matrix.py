def search_2d_martix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_val = matrix[mid // n][mid % n]
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def test_search_2d_matrix():
    assert search_2d_martix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    assert search_2d_martix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 20)
    assert search_2d_martix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 23)
    assert not search_2d_martix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], -15)
    assert not search_2d_martix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
    assert not search_2d_martix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 123)
    assert search_2d_martix([[1], [2]], 1)
