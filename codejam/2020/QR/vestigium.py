from collections import defaultdict
T = int(input())
for x in range(1, T + 1):
    N = int(input())
    k, r, c = 0, 0, 0
    colset = defaultdict(set)
    for row in range(N):
        rowset = set()
        row_elems = list(map(int, input().split()))
        for col in range(N):
            colset[col].add(row_elems[col])
            rowset.add(row_elems[col])
            if row == col:
                k += row_elems[col]
        if len(rowset) != N:
            r += 1
    for col in range(N):
        if len(colset[col]) != N:
            c += 1
    print('Case #{}: {} {} {}'.format(x, k, r, c))
