def add_binary(a, b):
    carry = 0
    ret = []
    n = max(len(a), len(b))
    a, b = a.zfill(n), b.zfill(n)
    for i in range(n - 1, -1, -1):
        carry = carry + 1 if a[i] == '1' else carry
        carry = carry + 1 if b[i] == '1' else carry
        if carry % 2 == 1:
            ret.append('1')
        else:
            ret.append('0')
        carry //= 2
    if carry:
        ret.append('1')
    ret.reverse()
    return ''.join(ret)


def test_add_binary():
    assert add_binary('11', '1') == '100'
    assert add_binary('101', '0') == '101'
    assert add_binary('10', '100') == '110'
    assert add_binary('0', '0') == '0'
