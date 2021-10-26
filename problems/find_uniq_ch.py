def find_uniq_ch(s):
    m = {}
    for i, ch in enumerate(s):
        if ch not in m:
            m[ch] = [i]
            continue
        m[ch].append(i)
    for _, ch in enumerate(s):
        if len(m[ch]) == 1:
            return m[ch][0]
    return -1


def test_find_uniq_ch():
    assert find_uniq_ch('abcaad') == 1
    assert find_uniq_ch('a') == 0
    assert find_uniq_ch('') == -1
    assert find_uniq_ch('aaa') == -1
