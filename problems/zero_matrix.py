def zero_matrix(m):
    n_rows = len(m)
    n_cols = len(m[0])
    flag_rows = [0] * n_rows
    flag_cols = [0] * n_cols
    for row in range(n_rows):
        for col in range(n_cols):
            if m[row][col] == 0:
                flag_rows[row] = 1
                flag_cols[col] = 1

    for row in range(n_rows):
        if flag_rows[row]:
            for col in range(n_cols):
                m[row][col] = 0
    for col in range(n_cols):
        if flag_cols[col]:
            for row in range(n_rows):
                m[row][col] = 0

if __name__ == "__main__":
    m = [[1, 2, 3, 4], [5, 0, 6, 7], [0, 8, 9, 10]]
    zero_matrix(m)
    for row in range(len(m)):
        print(m[row][:])
