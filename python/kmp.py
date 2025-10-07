def create_table(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def test_create_table():
    pattern = "ABACABA"
    expected_lps = [0, 0, 1, 0, 1, 2, 3]
    assert create_table(pattern) == expected_lps


def kmp_search(text, pattern):
    M, N = len(pattern), len(text)
    if M == 0:
        return 0
    if N < M:
        return -1

    lps = create_table(pattern)
    i, j = 0, 0

    while i < N:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        if j == M:
            return i - j

    return -1


def test_kmp_search():
    text = "ABABDABACDABABCABAB"
    pattern = "ABABC"
    assert kmp_search(text, pattern) == 10
