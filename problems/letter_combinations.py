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
    
    def combinations(digits, head):
        if len(digits[head:]) == 1:
            return letters[digits[head]]
        res = []
        for c in combinations(digits, head + 1):
            for l in letters[digits[head]]:
                res.append(''.join([l, c]))
        return res
    
    return combinations(digits, 0) if len(digits) != 0 else []