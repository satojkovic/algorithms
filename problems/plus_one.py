def plus_one(digits):
    res = len(digits) * [0]
    carry = 1
    for i in reversed(range(len(digits))):
        digit = digits[i] + carry
        res[i] = digit % 10
        carry = digit // 10
    return res if carry == 0 else [1] + res