def len_of_last_word(s):
    # Trim the trailing spaces
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    # Compute the length of the last word
    ret = 0
    while i >= 0 and s[i] != ' ':
        i -= 1
        ret += 1
    return ret


def test_len_of_last_word():
    assert len_of_last_word("a aa bb ccc") == 3
    assert len_of_last_word("aaaa") == 4
    assert len_of_last_word("  a  bb ") == 2
    assert len_of_last_word("") == 0
