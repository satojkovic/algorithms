def characterReplacement(s: str, k: int) -> int:
    left = 0
    max_len = 0
    char_count = {}
    for right in range(len(s)):
        char_count[s[right]] = 1 + char_count.get(s[right], 0)
        while is_valid_substr(left, right, char_count, k):
            char_count[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

def is_valid_substr(left, right, char_count, k):
    return right - left + 1 - max(char_count.values()) > k


def test_characterReplacement():
    assert characterReplacement("AABABBA", 1) == 4
    assert characterReplacement("AABABBA", 2) == 5
    assert characterReplacement("AABABBA", 0) == 2
    assert characterReplacement("A", 0) == 1
    assert characterReplacement("ABAB", 2) == 4
    assert characterReplacement("AAABBB", 2) == 5
