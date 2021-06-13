def make_equal(words):
    n = len(words)
    freqs = {}
    for word in words:
        for ch in word:
            if not ch in freqs:
                freqs[ch] = 1
            else:
                freqs[ch] += 1
    for k in freqs.keys():
        if freqs[k] % n != 0:
            return False
    return True


def test_make_equal():
    assert make_equal(['abc', 'aabc', 'bc']) == True
    assert make_equal(['ab', 'b']) == False
    assert make_equal(['bdefff']) == True
