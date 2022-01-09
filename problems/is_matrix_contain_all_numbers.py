def is_matrix_contain_all_numbers(matrix):
    n = len(matrix)
    for row_vals, col_vals in zip(matrix, zip(*matrix)):
        if len(set(row_vals)) != n or len(set(col_vals)) != n:
            return False
    return True


def test_is_matrix_contain_all_numbers():
    assert is_matrix_contain_all_numbers(
        [[1, 2, 3], [3, 1, 2], [2, 3, 1]]) == True
    assert is_matrix_contain_all_numbers([[1, 2], [1, 2]]) == False
    assert is_matrix_contain_all_numbers([[1, 1], [2, 2]]) == False
    assert is_matrix_contain_all_numbers([[1]]) == True
