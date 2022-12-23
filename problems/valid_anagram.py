# Time complexity: O(n + m)
#  length of the input s and t is n and m respectively.
#  iterate over s once, and also iterate over t once, array insertion is O(1).
#  sum of the array is O(1) because of the length of the array is fixed.
# Space complexity: O(1)
def valid_anagram(s, t):
    used = 256 * [0]
    for ch in s:
        used[ord(ch)] += 1
    for ch in t:
        if used[ord(ch)] == 0:
            return False
        else:
            used[ord(ch)] -= 1
    return True if sum(used) == 0 else False


def valid_anagram2(s, t):
    from collections import defaultdict
    chars = defaultdict(int)
    for c in s:
        chars[c] += 1
    for c in t:
        if chars[c] == 0:
            return False
        else:
            chars[c] -= 1
    return True if sum([v for _, v in chars.items()]) == 0 else False


def test_valid_anagram():
    assert valid_anagram('anagram', 'nagaram') is True
    assert valid_anagram('rat', 'car') is False
    assert valid_anagram('', 'abc') is False
    assert valid_anagram('abc', '') is False
    assert valid_anagram('', '') is True


def test_valid_anagram2():
    assert valid_anagram2('anagram', 'nagaram') is True
    assert valid_anagram2('rat', 'car') is False
    assert valid_anagram2('', 'abc') is False
    assert valid_anagram2('abc', '') is False
    assert valid_anagram2('', '') is True
