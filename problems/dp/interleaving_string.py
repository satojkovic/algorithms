from typing import List

def isInterleave(s1: str, s2: str, s3: str) -> bool:
    rows = len(s1)
    cols = len(s2)
    l3 = len(s3)
    if rows + cols != l3:
        return False
    dp = [[False] * (cols + 1) for _ in range(rows + 1)]
    dp[0][0] = True

    for i in range(rows + 1):
        for j in range(cols + 1):
            if i == 0 and j == 0:
                continue
            can_come_from_top = False
            can_come_from_left = False

            if i > 0 and dp[i-1][j] and s1[i-1] == s3[i + j - 1]:
                can_come_from_top = True
            if j > 0 and dp[i][j-1] and s2[j-1] == s3[i + j - 1]:
                can_come_from_left = True

            if can_come_from_top or can_come_from_left:
                dp[i][j] = True

    return dp[rows][cols]


def test_isInterleave():
    assert isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
    assert isInterleave("aabcc", "dbbca", "aadbbbaccc") == False
    assert isInterleave("", "", "") == True
    assert isInterleave("ab", "cd", "ac") == False
