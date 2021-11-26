def strstr(haystack, needle):
    if len(needle) == 0:
        return 0
    k = len(needle)
    res = -1
    for i in range(len(haystack) - k + 1):
        if haystack[i:i+k] == needle:
            res = i
            break
    return res


def test_strstr():
    assert strstr('test', 'st') == 2
    assert strstr('abcde', 'abd') == -1
    assert strstr('abc', '') == 0
    assert strstr('', '') == 0
    assert strstr('', 'x') == -1
