def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

def reverse_str(s):
    if len(s) == 0:
        return s
    rstr = reverse_str(s[1:])
    return ''.join([rstr, s[0]])

def reverse_str2(s):
    if len(s) == 0:
        return []
    rstr = reverse_str2(s[1:])
    return rstr + [s[0]]

def reverse_str3(s, head, tail):
    if head >= tail:
        return
    s[head], s[tail] = s[tail], s[head]
    return reverse_str3(s, head + 1, tail - 1)