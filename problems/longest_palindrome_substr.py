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


def dp(s):
    def check(s, dp, i, j):
        if i == j:
            return True
        elif i + 1 == j:
            return s[i] == s[j]
        else:
            return dp[i+1][j-1] and s[i] == s[j]

    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    max_start_pos, max_len = 0, 1
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if check(s, dp, i, j):
                dp[i][j] = True
                cand_len = j - i + 1
                if cand_len > max_len:
                    max_len = cand_len
                    max_start_pos = i
    return s[max_start_pos:max_start_pos + max_len]


def test_dp():
    assert dp('babad') == 'bab' or dp('babad') == 'aba'
    assert dp('cbbd') == 'bb'
    assert dp('a') == 'a'
    assert dp('ac') == 'a' or dp('ac') == 'c'
    assert dp('aaaa') == 'aaaa'
    assert dp('89255') == '55'
