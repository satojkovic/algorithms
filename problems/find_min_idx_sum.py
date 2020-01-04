def find_min_idx_sum(list1, list2):
    common = set(list1) & set(list2)
    if len(common) == 1:
        return list(common)
    d1 = {k:i for i, k in enumerate(list1)}
    d2 = {k:i for i, k in enumerate(list2)}
    res = {}
    min_idx_sum = len(list1) + len(list2) + 1
    for c in common:
        idx_sum = d1[c] + d2[c]
        if not idx_sum in res:
            res[idx_sum] = [c]
        else:
            res[idx_sum].append(c)
        if idx_sum < min_idx_sum:
            min_idx_sum = idx_sum
    return res[min_idx_sum]
