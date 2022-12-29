from src.group_anagram_words import *


def test_group_anagram_words2():
    ret = group_anagram_words2(["eat","tea","tan","ate","nat","bat"])
    ans = [["eat","tea","ate"],["tan","nat"],["bat"]]
    assert len(ret) == len(ans)
    assert all([sorted(r) == sorted(a)] for r, a in zip(sorted(ret), sorted(ans)))
