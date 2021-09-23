def plus_one(digits):
    carry = 1
    for i in reversed(range(len(digits))):
        digit = digits[i] + carry
        digits[i] = digit % 10
        carry = digit // 10
    return digits if carry == 0 else [1] + digits


def plus_one2(digits):
    n = int(''.join([str(d) for d in digits]))
    n += 1
    return [int(a) for a in str(n)]


def test_plus_one2():
    assert plus_one2([1, 2, 3]) == [1, 2, 4]
    assert plus_one2([9, 9]) == [1, 0, 0]
    assert plus_one2([0]) == [1]
