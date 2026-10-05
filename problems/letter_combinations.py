def letter_combinations(digits):
    letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def backtrack(bucket, candidates):
        if bucket == len(digits):
            res.append(''.join(candidates))
            return

        num = digits[bucket]
        for letter in letters[num]:
            candidates.append(letter)
            backtrack(bucket + 1, candidates)
            candidates.pop()

    res = []
    backtrack(0, [])
    return res

def test_letter_combinations():
    assert letter_combinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert letter_combinations("2") == ["a", "b", "c"]
    assert letter_combinations("234") == ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
