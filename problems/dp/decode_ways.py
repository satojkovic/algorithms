def numDecodings(s: str) -> int:
    N = len(s)
    dp = (N + 1) * [0]
    dp[0] = 1

    for i in range(1, N + 1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]

        if i >= 2:
            two_digit = s[i-2:i]
            if '10' <= two_digit <= '26':
                dp[i] += dp[i-2]

    return dp[N]


def test_numDecodings():
    assert numDecodings('12') == 2
    assert numDecodings('226') == 3
    assert numDecodings('06') == 0
