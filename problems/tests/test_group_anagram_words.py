from src.group_anagram_words import *


def test_group_anagram_words2():
    assert group_anagram_words2(["eat","tea","tan","ate","nat","bat"]) == [["eat","tea","ate"],["tan","nat"],["bat"]]
