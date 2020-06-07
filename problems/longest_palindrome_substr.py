def longest_palindrome_substr(s):
    N = len(s)
    for n in range(N, 1, -1):
        for i in range(N):
            if i + n > N:
                break
            if is_palindrome(s[i:i+n]):
                return s[i:i+n]
    return s[0] if N > 0 else s

def is_palindrome(s):
    def check(s, head, tail):
        if head > tail:
            return True
        if s[head] != s[tail]:
            return False
        return check(s, head + 1, tail - 1)
    return check(s, 0, len(s) - 1)

if __name__ == "__main__":
    print(longest_palindrome_substr('abcdad'))