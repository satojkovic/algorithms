def brute_force(s):
    def check(s, i, j):
        left, right = i, j
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    ret = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            if check(s, i, j) and len(ret) < j - i + 1:
                ret = s[i:j+1]
    return ret


def test_brute_force():
    assert brute_force('babad') == 'bab'
    assert brute_force('cbbd') == 'bb'
    assert brute_force('a') == 'a'
    assert brute_force('ac') == 'a'
    assert brute_force('aaaa') == 'aaaa'
    assert brute_force('89255') == '55'
