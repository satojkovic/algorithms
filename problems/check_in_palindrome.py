def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1_freq = {}
    s2_freq = {}

    for i in range(len(s1)):
        s1_freq[s1[i]] = 1 + s1_freq.get(s1[i], 0)
        s2_freq[s2[i]] = 1 + s2_freq.get(s2[i], 0)
    if s1_freq == s2_freq:
        return True

    left = 0
    for right in range(len(s1), len(s2)):
        s2_freq[s2[right]] = 1 + s2_freq.get(s2[right], 0)
        s2_freq[s2[left]] -= 1
        if s2_freq[s2[left]] == 0:
            del s2_freq[s2[left]]
        left += 1
        if s1_freq == s2_freq:
            return True
    return False

def checkInclusion2(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1_freq = [0] * 26
    s2_freq = [0] * 26

    for i in range(len(s1)):
        s1_freq[ord(s1[i]) - ord('a')] += 1
        s2_freq[ord(s2[i]) - ord('a')] += 1
    if s1_freq == s2_freq:
        return True

    left = 0
    for right in range(len(s1), len(s2)):
        s2_freq[ord(s2[right]) - ord('a')] += 1
        s2_freq[ord(s2[left]) - ord('a')] -= 1
        left += 1
        if s1_freq == s2_freq:
            return True
    return False

def test_checkInclusion():
    assert checkInclusion("ab", "eidbaooo") == True
    assert checkInclusion("ab", "eidboaoo") == False
    assert checkInclusion("abc", "ccccbbbbaaaa") == False
    assert checkInclusion("abc", "cccbaaa") == True
    assert checkInclusion("a", "a") == True
    assert checkInclusion("a", "b") == False
    assert checkInclusion("", "") == True

def test_checkInclusion2():
    assert checkInclusion2("ab", "eidbaooo") == True
    assert checkInclusion2("ab", "eidboaoo") == False
    assert checkInclusion2("abc", "ccccbbbbaaaa") == False
    assert checkInclusion2("abc", "cccbaaa") == True
    assert checkInclusion2("a", "a") == True
    assert checkInclusion2("a", "b") == False
    assert checkInclusion2("", "") == True
