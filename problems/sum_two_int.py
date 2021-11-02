def sum_two_int(a, b):
    mask = 0xFFFFFFFF
    while not b == 0:
        carry = a & b
        a = (a ^ b) & mask
        b = (carry << 1) & mask

    if a > 2**31:
        return ~(a ^ mask)
    else:
        return a


def test_sum_two_int():
    assert sum_two_int(1, 2) == 3
    assert sum_two_int(0, 4) == 4
    assert sum_two_int(12, 0) == 12
    assert sum_two_int(0, 0) == 0
    assert sum_two_int(-1, 3) == 2
    assert sum_two_int(-18, -125) == -143
