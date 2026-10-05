def partition(s: str) -> list[list[str]]:
    def is_palindrome(substr):
        return substr == substr[::-1]

    res = []
    def backtrack(start, path):
        if start == len(s):
            res.append(list(path))
            return

        for end in range(start + 1, len(s) + 1):
            substr = s[start:end]
            if not is_palindrome(substr):
                continue
            path.append(substr)
            backtrack(end, path)
            path.pop()

    backtrack(0, [])
    return res


def test_parition():
    assert partition("aab") == [["a","a","b"],["aa","b"]]
    assert partition("a") == [["a"]]
