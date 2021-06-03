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
    import math
    is_prime_flags = [0] * (n+1)
    primes = []
    for i in range(2, n):
        if is_prime_flags[i] == 0:
            primes.append(i)
            for j in range(i + i, n, i):
                is_prime_flags[j] = 1
    return len(primes)


if __name__ == '__main__':
    print(count_prime_number_bruteforce(10))
    print(count_prime_number_bruteforce(1))
    print(count_prime_number_bruteforce(0))
