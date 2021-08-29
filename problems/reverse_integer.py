def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x = str(abs(x))
    res = sign * int(x[::-1])
    return res if -2**31 <= res <= 2**31-1 else 0


def test_reverse_integer():
    assert reverse_integer(123) == 321
    assert reverse_integer(-456) == -654
    assert reverse_integer(0) == 0
    assert reverse_integer(890) == 98
