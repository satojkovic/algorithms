def rotate(matrix):
    def rot(matrix, i, j):
        def swap(matrix, a, b):
            matrix[a[0]][a[1]], matrix[b[0]][b[1]] = (
                matrix[b[0]][b[1]],
                matrix[a[0]][a[1]],
            )

        curr_pos = (i, j)
        next_pos = (j, n - i - 1)
        prev_pos = (n - j - 1, i)
        mid_pos = (n - i - 1, n - j - 1)
        # swap
        swap(matrix, curr_pos, prev_pos)
        swap(matrix, prev_pos, mid_pos)
        swap(matrix, mid_pos, next_pos)

    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            rot(matrix, i, j)


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
