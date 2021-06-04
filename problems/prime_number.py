import math


def count_prime_number_bruteforce(n):
    count = 0
    for p in range(2, n):
        if is_prime(p):
            count += 1
    return count


def is_prime(p):
    if p == 1:
        return False
    for k in range(2, int(math.sqrt(p)) + 1):
        if p % k == 0:
            return False
    return True


def count_prime_number_eratosthenes(n):
    primes = {i for i in range(2, n)}
    for i in range(2, n):
        if i in primes:
            for j in range(i * 2, n, i):
                if j in primes:
                    primes.remove(j)
    return len(primes)


def count_prime_number_eratosthenes_list(n):
    primes = [0] * 2 + [1] * (n - 2)
    for i in range(2, n):
        if primes[i]:
            for j in range(i * 2, n, i):
                primes[j] = 0
    return sum(primes)


if __name__ == '__main__':
    print(count_prime_number_bruteforce(10))
    print(count_prime_number_bruteforce(1))
    print(count_prime_number_bruteforce(0))
