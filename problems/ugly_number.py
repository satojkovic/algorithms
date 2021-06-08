import heapq


def ugly_number(n):
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    q = [1]
    seen = {1}
    for i in range(n-1):
        u = heapq.heappop(q)
        for nu in [2*u, 3*u, 5*u]:
            if not nu in seen:
                heapq.heappush(q, nu)
                seen.add(nu)
    return heapq.heappop(q)


def is_ugly(n):
    if n <= 0:
        return False
    for p in [2, 3, 5]:
        while n % p == 0:
            n = n // p
    return n == 1


if __name__ == '__main__':
    print(ugly_number(10))
    print(is_ugly(6), is_ugly(7), is_ugly(8), is_ugly(1))
