def solution1():
    N = input().rstrip()
    org_N = int(N)
    N = list(N)
    cands = []
    for i in range(len(N), -1, -1):
        for j in range(10):
            n = N[:i] + [str(j)] + N[i:]
            n = int(''.join(n))
            if n != org_N and n % 9 == 0:
                cands.append(n)
    print('Case #{}: {}'.format(t, min(cands)))


def insert_digit(N, d, k):
    return (N - N % 10**k) * 10 + d * 10**k + (N % 10**k)


def insert_digit_with_slice(N, d, k):
    N = list(str(N))
    n = N[:k] + [str(d)] + N[k:]
    return int(''.join(n))


def solution2():
    import math
    N = int(input().rstrip())
    L = len(str(N))
    cands = []
    for i in range(L + 1):
        for j in range(10):
            n = insert_digit(N, j, i)
            if n != N and n % 9 == 0:
                cands.append(n)
    print('Case #{}: {}'.format(t, min(cands)))


def which_digit_to_insert(N):
    sum_n = sum(list(map(int, list(str(N)))))
    return 9 - sum_n % 9 if sum_n % 9 != 0 else 0


def where_to_insert(N, d):
    def get_digits(N):
        if N < 10:
            return [N]
        ret = get_digits(N // 10)
        ret.append(N % 10)
        return ret

    def get_digits_iter(N, L):
        digits = []
        rem = N
        while L >= 1:
            d = rem // 10**(L-1)
            rem = rem % 10**(L-1)
            digits.append(d)
            L = L - 1
        return digits
    k = 0
    L = len(str(N))
    digits = get_digits_iter(N, L)
    for i, digit in enumerate(digits):
        if digit > d:
            break
        k += 1
    return k + 1 if d == 0 and k == 0 else k


def solution3():
    import math
    N = int(input().rstrip())
    d = which_digit_to_insert(N)
    k = where_to_insert(N, d)
    print('Case #{}: {}'.format(t, insert_digit_with_slice(N, d, k)))


T = int(input())
for t in range(1, T + 1):
    solution3()
