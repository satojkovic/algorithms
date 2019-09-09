def four_sum_count1(A, B, C, D):
    ab = {}
    for a in A:
        for b in B:
            if -a-b in ab:
                ab[-a-b] += 1
            else:
                ab[-a-b] = 1
    ret = 0
    for c in C:
        for d in D:
            if c + d in ab:
                ret += ab[c+d]
    return ret    