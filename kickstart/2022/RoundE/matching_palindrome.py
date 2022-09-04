def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    P = input().rstrip()
    for i in range(N):
        q = P[:i+1]
        if is_palindrome(q) and is_palindrome(P + q):
            print('Case #{}: {}'.format(t, q))
            break
        