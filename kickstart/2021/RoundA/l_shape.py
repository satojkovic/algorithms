def cumsum_matrix(mat):
    rows, cols = len(mat), len(mat[0])
    cumsum_mat = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            cumsum_mat[r][c] = cumsum_mat[r][c-1] + mat[r][c] \
                if c != 0 else mat[r][c]
    return cumsum_mat


def prefixsum_matrix(mat):
    rows, cols = len(mat), len(mat[0])
    cumsum_mat = cumsum_matrix(mat)
    prefixsum_mat = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            prefixsum_mat[r][c] = prefixsum_mat[r-1][c] + cumsum_mat[r][c] \
                if r != 0 else cumsum_mat[r][c]
    return prefixsum_mat


def segment_one_count(lt_row, lt_col, rb_row, rb_col, prefixsum_mat):
    a = prefixsum_mat[rb_row][rb_col]
    b = prefixsum_mat[rb_row][lt_col-1] if lt_col > 0 else 0
    c = prefixsum_mat[lt_row-1][rb_col] if lt_row > 0 else 0
    d = prefixsum_mat[lt_row-1][lt_col-1] if lt_row > 0 and lt_col > 0 else 0
    return (a - b - c + d)


def is_len_cond(lt_row, lt_col, rb_row, rb_col):
    return abs(rb_col - lt_col) + 1 == 2 * (abs(rb_row - lt_row) + 1) or \
        2 * (abs(rb_col - lt_col) + 1) == abs(rb_row - lt_row) + 1


def check(R, C, prefixsum_mat):
    import itertools
    res = 0
    for (i, j) in itertools.product(range(R), range(C)):
        for (k, l) in itertools.product(range(R), range(C)):
            if segment_one_count(i, j, i, l, prefixsum_mat) == (abs(l - j) + 1) and \
                segment_one_count(k, l, i, l, prefixsum_mat) == (abs(k - i) + 1) and \
                is_len_cond(i, j, k, l):
                res += 1
            if segment_one_count(i, j, k, j, prefixsum_mat) == (abs(k - i) + 1) and \
                segment_one_count(k, j, k, l, prefixsum_mat) == (abs(l - j) + 1) and \
                is_len_cond(i, j, k, l):
                res += 1
    return res // 2


def solve2():
    T = int(input())
    for t in range(1, T + 1):
        R, C = list(map(int, input().split()))
        mat = [list(map(int, input().split())) for _ in range(R)]
        prefixsum_mat = prefixsum_matrix(mat)
        res = check(R, C, prefixsum_mat)
        print('Case #{}: {}'.format(t, res))


def solve1():
    import math

    def get_row_seg_len(mat, start, end, step, c):
        seg_len = 0
        for i in range(start, end, step):
            if mat[i][c] == 0:
                break
            seg_len += 1
        return seg_len

    def get_col_seg_len(mat, start, end, step, r):
        seg_len = 0
        for i in range(start, end, step):
            if mat[r][i] == 0:
                break
            seg_len += 1
        return seg_len

    def get_seg_lens(mat, r, c, R, C):
        # order: upper, lower, left, right
        seg_lens = []
        seg_lens.append(get_row_seg_len(mat, r, -1, -1, c))
        seg_lens.append(get_row_seg_len(mat, r, R, 1, c))
        seg_lens.append(get_col_seg_len(mat, c, -1, -1, r))
        seg_lens.append(get_col_seg_len(mat, c, C, 1, r))
        return seg_lens

    def get_row_count(row_seg, col_seg, R, C):
        count = 0
        if row_seg >= 4 and col_seg >= 2:
            count = min(math.floor((row_seg - 4) / 2) + 1, col_seg - 1)
        return count

    def get_col_count(row_seg, col_seg, R, C):
        count = 0
        if row_seg >= 2 and col_seg >= 4:
            count = min(row_seg - 1, math.floor((col_seg - 4) / 2) + 1)
        return count

    from itertools import product
    def count_l_shape(seg_lens, R, C):
        count = 0
        for row_seg, col_seg in product(seg_lens[:2], seg_lens[2:]):
            count += get_row_count(row_seg, col_seg, R, C)
            count += get_col_count(row_seg, col_seg, R, C)
        return count

    # main loop
    # Test set1: Passed
    # Test set2: TLE
    T = int(input())
    for t in range(1, T + 1):
        R, C = list(map(int, input().split()))
        mat = []
        for r in range(R):
            mat.append(list(map(int, input().split())))
        res = 0
        for r in range(R):
            for c in range(C):
                seg_lens = get_seg_lens(mat, r, c, R, C)
                res += count_l_shape(seg_lens, R, C) 
        print('Case #{}: {}'.format(t, res))


if __name__ == '__main__':
    solve2()
