def zigzag(s, num_rows):
    ret = [[] for _ in range(num_rows)]
    i = 0
    while i < len(s):
        idx = 0
        while idx < num_rows and i < len(s):
            ret[idx].append(s[i])
            i += 1
            idx += 1
        idx = num_rows - 2
        while idx >= 1 and i < len(s):
            ret[idx].append(s[i])
            i += 1
            idx -= 1
    return ''.join([c for r in ret for c in r])


def test_zigzag():
    assert zigzag('abcdefg', 2) == 'acegbdf'
    assert zigzag('abcdefg', 3) == 'aebdfcg'
    assert zigzag('abcdefg', 4) == 'agbfced'
    assert zigzag('abc', 4) == 'abc'
    assert zigzag('.', 1) == '.'
