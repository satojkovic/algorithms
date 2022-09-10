def cumsum_matrix(mat):
    rows, cols = len(mat), len(mat[0])
    cumsum_mat = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            cumsum_mat[r][c] = cumsum_mat[r][c-1] + mat[r][c] \
                if c != 0 else mat[r][c]
    return cumsum_mat

def test_cumsum_matrix():
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    cumsum_mat = cumsum_matrix(mat)
    assert cumsum_mat == [
        [1, 3, 6, 10],
        [5, 11, 18, 26],
        [9, 19, 30, 42]
    ]

    mat = [
        [1],
        [2],
        [3]
    ]
    cumsum_mat = cumsum_matrix(mat)
    assert cumsum_mat == [
        [1],
        [2],
        [3]
    ]

    mat = [[10]]
    cumsum_mat = cumsum_matrix(mat)
    assert cumsum_mat == [[10]]

    mat = [
        [1, 2, 3, 4, 6],
        [5, 3, 8, 1, 2],
        [4, 6, 7, 5, 5],
        [2, 4, 8, 9, 4]
    ]
    cumsum_mat = cumsum_matrix(mat)
    assert cumsum_mat == [
        [1, 3, 6, 10, 16],
        [5, 8, 16, 17, 19],
        [4, 10, 17, 22, 27],
        [2, 6, 14, 23, 27]
    ]



def prefixsum_matrix(mat):
    rows, cols = len(mat), len(mat[0])
    cumsum_mat = cumsum_matrix(mat)
    prefixsum_mat = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            prefixsum_mat[r][c] = prefixsum_mat[r-1][c] + cumsum_mat[r][c] \
                if r != 0 else cumsum_mat[r][c]
    return prefixsum_mat

def test_prefixsum_matrix():
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    prefixsum_mat = prefixsum_matrix(mat)
    assert prefixsum_mat == [
        [1, 3, 6, 10],
        [6, 14, 24, 36],
        [15, 33, 54, 78]
    ]

    mat = [
        [1],
        [2],
        [3]
    ]
    prefixsum_mat = prefixsum_matrix(mat)
    assert prefixsum_mat == [
        [1],
        [3],
        [6]
    ]

    mat = [[10]]
    prefixsum_mat = prefixsum_matrix(mat)
    assert prefixsum_mat == [[10]]

    mat = [
        [1, 2, 3, 4, 6],
        [5, 3, 8, 1, 2],
        [4, 6, 7, 5, 5],
        [2, 4, 8, 9, 4]
    ]
    prefixsum_mat = prefixsum_matrix(mat)
    assert prefixsum_mat == [
        [1, 3, 6, 10, 16],
        [6, 11, 22, 27, 35],
        [10, 21, 39, 49, 62],
        [12, 27, 53, 72, 89]
    ]
