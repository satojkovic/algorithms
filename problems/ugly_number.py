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


if __name__ == '__main__':
    print(ugly_number(10))
