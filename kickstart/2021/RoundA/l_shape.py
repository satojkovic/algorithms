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
    solve1()
