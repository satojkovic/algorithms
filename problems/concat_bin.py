def concat_bin(n):
    import math
    ret = 0
    modulo = 10 ** 9 + 7
    for i in range(1, n + 1):
        digit = math.floor(math.log2(i)) + 1
        ret = (ret * (2 ** digit) + i) % modulo
    return ret


def test_concat_bin():
    assert concat_bin(1) == 1
    assert concat_bin(2) == 6
    assert concat_bin(3) == 27
    assert concat_bin(4) == 220
    assert concat_bin(12) == 505379714
