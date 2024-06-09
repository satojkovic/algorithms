def is_palindrome(s):
    s = ''.join(filter(lambda c: c.isalnum(), s)).lower()
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def is_palindrome2(x):
    # Time complexity: O(log10(x))
    # Space complexity: O(1)
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    revert_num = 0
    while x > revert_num:
        revert_num = revert_num * 10 + x % 10
        x = x // 10
    return x == revert_num or x == revert_num // 10


def is_palindrome3(s):
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not is_alpha_numeric(s[l]):
            l += 1
        while r > l and not is_alpha_numeric(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


def is_alpha_numeric(c):
    return (
        ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
    )


def test_is_palindrome3():
    assert is_palindrome3("Was it a car or a cat I saw?") is True
    assert is_palindrome3("tab a cat") is False
    assert is_palindrome3("A") is True
    assert is_palindrome3("abc") is False
    assert is_palindrome3("abcd") is False


def test_is_palindrome2():
    assert is_palindrome2(12321) == True
    assert is_palindrome2(120) == False
    assert is_palindrome2(1221) == True
    assert is_palindrome2(-121) == False


if __name__ == '__main__':
    print(is_palindrome('aba'))
    print(is_palindrome('1234321'))
    print(is_palindrome(''))
    print(is_palindrome('Abc'))
    print(is_palindrome('2-0-2-0'))
    print(is_palindrome('2,0,0,2'))
