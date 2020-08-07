def largest_island(mat):
    def _dfs(mat, row, col, n_rows, n_cols, count):
        if row < 0 or col < 0 or row >= n_rows or col >= n_cols or mat[row][col] != 1:
            return count
        count += 1
        mat[row][col] = 2
        count = _dfs(mat, row + 1, col, n_rows, n_cols, count)
        count = _dfs(mat, row, col + 1, n_rows, n_cols, count)
        count = _dfs(mat, row - 1, col, n_rows, n_cols, count)
        count = _dfs(mat, row, col - 1, n_rows, n_cols, count)
        return count

    ret = 0
    n_rows, n_cols = len(mat), len(mat[0])
    for row in range(n_rows):
        for col in range(n_cols):
            if mat[row][col] != 1:
                continue
            count = _dfs(mat, row, col, n_rows, n_cols, 0)
            ret = count if ret < count else ret
    return ret
