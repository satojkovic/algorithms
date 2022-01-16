from __future__ import division


def divide_and_group(s, k, fill):
    ret = []
    i = 0
    while i < len(s) - k:
        ret.append(''.join(s[i:i+k]))
        i += k
    if len(s) % k != 0:
        ret.append(''.join(s[i:]) + fill * (k - len(s) % k))
    else:
        ret.append(''.join(s[i:]))
    return ret


def test_divide_and_group():
    assert divide_and_group('abcd', 3, 'x') == ['abc', 'dxx']
    assert divide_and_group('abcd', 2, 'x') == ['ab', 'cd']
    assert divide_and_group('e', 5, 'x') == ['exxxx']
