def most_common_word(paragraph, banned):
    import string
    for p in string.punctuation:
        paragraph = paragraph.replace(p, ' ')
    paragraph = paragraph.lower()
    banned = set(banned)
    word_count = {}
    max_count = 0
    res = ''
    for p in paragraph.split():
        if p in banned:
            continue
        if p in word_count:
            word_count[p] += 1
        else:
            word_count[p] = 1
        if word_count[p] > max_count:
            max_count = word_count[p]
            res = p
    return res


def test_most_common_word():
    print(most_common_word("a.", []))
    print(most_common_word(
        "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
