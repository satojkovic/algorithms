def group_anagram_words(words):
    g = {}
    for word in words:
        count = [0] * 26
        for c in word:
            index = ord(c) - ord('a')
            count[index] += 1
        key = tuple(count)
        if key in g:
            g[key].append(word)
        else:
            g[key] = [word]
    return g.values()


if __name__ == '__main__':
    print(list(group_anagram_words(['abf', 'bc', 'cb', 'fab', 'aaa', 'baf'])))
