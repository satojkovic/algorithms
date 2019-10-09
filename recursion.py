def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

def reverse_str(s):
    if len(s) == 0:
        return s
    rstr = reverse_str(s[1:])
    return rstr + s[0]