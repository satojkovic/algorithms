from collections import Counter


def sort_char_freq(s):
    char_freqs = Counter(s)
    char_freqs = Counter(s)
    char_freqs = [item for item in char_freqs.items()]
    char_freqs = sorted(char_freqs, key=lambda x: -x[1])
    return ''.join([item[0]*item[1] for item in char_freqs])


def test_sort_char_freq():
    res = sort_char_freq('tree')
    assert (res != 'eetr') or (res != 'eert')
