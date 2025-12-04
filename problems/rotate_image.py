def rotate(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        for i in range(layer, n - 1 -layer):
            top = matrix[layer][i]
            matrix[layer][i] = matrix[n - 1 - i][layer]
            matrix[n - 1 - i][layer] = matrix[n - 1 -layer][n - 1 - i]
            matrix[n - 1 - layer][n - 1 - i] = matrix[i][n - 1 - layer]
            matrix[i][n - 1 - layer] = top

def rotate_eq_transpose_and_reverse(matrix):
    n = len(matrix)
    for row in range(n):
        for col in range(row + 1, n):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in range(n):
        for col in range(n // 2):
            matrix[row][col], matrix[row][n - 1 - col] = matrix[row][n - 1- col], matrix[row][col]



def test_rotate_image():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    rotate(matrix)
    assert matrix == [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5],
    ]


def test_rotate_eq_transpose_reverse():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_eq_transpose_and_reverse(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    rotate_eq_transpose_and_reverse(matrix)
    assert matrix == [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5],
    ]
