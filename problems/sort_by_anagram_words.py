from collections import defaultdict


def sort_by_anagram_words0(arr):
    # time complexity: O(klog(k) * nlog(n))
    # space complexity: O(n)
    return sorted(arr, key=lambda x: sorted(x))


def sort_by_anagram_words(arr):
    # time complexity: O(nklog(k))
    # space complexity: O(n)
    anagrams = defaultdict(list)
    for a in arr:
        sig_a = ''.join(sorted(a))
        anagrams[sig_a].append(a)

    pos = 0
    for key in anagrams.keys():
        for anagram in anagrams[key]:
            arr[pos] = anagram
            pos += 1
    return arr


def test_sort_by_anagram_words():
    assert sort_by_anagram_words0(['acb', 'cd', 'bac', 'cba', 'dc', 'aaac']) == [
        'aaac', 'acb', 'bac', 'cba', 'cd', 'dc']

    assert sort_by_anagram_words0(['aaa', 'abb', 'aaa']) == [
        'aaa', 'aaa', 'abb']

    assert sort_by_anagram_words(['acb', 'cd', 'bac', 'cba', 'dc', 'aaac']) == [
        'acb', 'bac', 'cba', 'cd', 'dc', 'aaac']

    assert sort_by_anagram_words(['aaa', 'abb', 'aaa']) == [
        'aaa', 'aaa', 'abb']
