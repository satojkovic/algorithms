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


if __name__ == '__main__':
    print(is_palindrome('aba'))
    print(is_palindrome('1234321'))
    print(is_palindrome(''))
    print(is_palindrome('Abc'))
    print(is_palindrome('2-0-2-0'))
    print(is_palindrome('2,0,0,2'))
