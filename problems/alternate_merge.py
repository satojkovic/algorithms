def alternate_merge(word1, word2):
    merged = []
    max_len = max(len(word1), len(word2))
    for i in range(max_len):
        ch = word1[i] if i < len(word1) else ""
        merged.append(ch)
        ch = word2[i] if i < len(word2) else ""
        merged.append(ch)
    return "".join(merged)


def test_alternate_merge():
    word1 = "abc"
    word2 = "def"
    assert alternate_merge(word1, word2) == "adbecf"

    word1 = "ab"
    word2 = "cdef"
    assert alternate_merge(word1, word2) == "acbdef"
