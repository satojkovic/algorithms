import math


def check(n):
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


def gen_primes(n):
    res = []
    for i in range(2, n + 1):
        if check(i):
            res.append(i)
            if i * i >= n:
                break
    return res


def binary_search(primes, left, right, Z):
    while left < right:
        mid = (left + right + 1) // 2
        if mid != len(primes) - 1 and primes[mid] * primes[mid + 1] <= Z:
            left = mid
        else:
            right = mid - 1
    return primes[left] * primes[left + 1]


T = int(input())
for t in range(1, T + 1):
    Z = int(input())
    primes = gen_primes(Z)
    print(primes)
    secret_code = binary_search(primes, 0, len(primes) - 1, Z)
    print('Case #{}: {}'.format(t, secret_code))
