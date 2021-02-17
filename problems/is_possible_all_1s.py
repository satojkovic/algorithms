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

if __name__ == '__main__':
    print(is_possible([8, 5]))
    print(is_possible([1, 1, 1, 2]))
    print(is_possible([9, 3, 5]))

        