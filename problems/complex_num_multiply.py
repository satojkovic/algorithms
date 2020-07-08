def complex_num_multiply(a, b):
    num_a1 = int(a.split('+')[0])
    num_b1 = int(a.split('+')[1][:-1])
    num_a2 = int(b.split('+')[0])
    num_b2 = int(b.split('+')[1][:-1])
    mult_former = num_a1 * num_a2 + (-1) * num_b1 * num_b2
    mult_latter = num_a1 * num_b2 + num_a2 * num_b1
    res = '+'.join([str(mult_former), str(mult_latter) + 'i'])
    return res