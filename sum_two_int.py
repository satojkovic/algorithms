def sum_two_int1(a, b):
    mask = 0xFFFFFFFF
    while not b == 0:
        carry = a & b
        a = (a^b) & mask
        b = (carry << 1) & mask

    if a > 2**31:
        return ~(a^mask)
    else:
        return a