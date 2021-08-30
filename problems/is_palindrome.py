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
