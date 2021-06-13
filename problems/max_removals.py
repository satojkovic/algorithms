def max_removals(s, p, removable):
    # search space is [0, len(removable)] (both inclusive)
    # because check function checks removable[:mid].
    return binary_search(s, p, removable, 0, len(removable))


def binary_search(s, p, removable, left, right):
    while left < right:
        mid = (left + right + 1) // 2
        if check(s, p, removable[:mid]):
            left = mid
        else:
            right = mid - 1
    return left


def check(s, p, removable):
    pidx = 0
    removable = set(removable)
    for i, ch in enumerate(s):
        if i in removable:
            continue
        if ch == p[pidx]:
            pidx += 1
        if pidx >= len(p):
            break
    return pidx == len(p)
