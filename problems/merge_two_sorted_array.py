def merge_two_sorted_array(a, b, a_size, b_size):
    last_a = a_size - 1
    last_b = b_size - 1
    last_merged = a_size + b_size - 1
    while last_b >= 0:
        if last_a >= 0 and a[last_a] >= b[last_b]:
            a[last_merged] = a[last_a]
            last_a -= 1
        else:
            a[last_merged] = b[last_b]
            last_b -= 1
        last_merged -= 1
    return a