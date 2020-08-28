def sort_by_anagram_words0(arr):
    return sorted(arr, key=lambda x: sorted(x))

from collections import defaultdict
def sort_by_anagram_words(arr):
    anagrams = defaultdict(list)
    for a in arr:
        sig_a = ''.join(sorted(a))
        anagrams[sig_a].append(a)

    pos = 0
    for sig in anagrams.keys():
        for a in anagrams[sig]:
            arr[pos] = a
            pos += 1
    return arr

if __name__ == "__main__":
    print(sort_by_anagram_words0(['acb', 'cd', 'bac', 'cba', 'dc', 'aaac']))
    print(sort_by_anagram_words(['acb', 'cd', 'bac', 'cba', 'dc', 'aaac']))