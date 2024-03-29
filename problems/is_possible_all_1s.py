def is_possible(target):
    if sum(target) == len(target):
        return True
    max_elem = max(target)
    max_elem_i = target.index(max_elem)
    rest = sum(target[:max_elem_i])
    rest = rest + sum(target[max_elem_i + 1:]) if max_elem_i != len(target) - 1 else rest
    before = max_elem - rest
    if before < 1:
        return False
    else:
        target[max_elem_i] = before
        return is_possible(target)

def is_possible_iter(target):
    import heapq
    total = sum(target)
    target = [-x for x in target]
    heapq.heapify(target)
    while -target[0] > 1:
        max_elem = -target[0]
        rest = total - max_elem
        if max_elem == 1 or rest == 1: # Special case: [1, 100000] is True
            return True
        if max_elem < rest or rest == 0 or max_elem % rest == 0:
            return False
        before = max_elem % rest
        total = total - max_elem + before
        heapq.heapreplace(target, -before)
    return True

if __name__ == '__main__':
    print(is_possible([8, 5]))
    print(is_possible_iter([8, 5]))
    print(is_possible([1, 1, 1, 2]))
    print(is_possible_iter([1, 1, 1, 2]))
    print(is_possible([9, 3, 5]))
    print(is_possible_iter([9, 3, 5]))

        