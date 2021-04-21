def counting_sort(A):
    max_A = 1000
    counts = [0 for _ in range(max_A + 1)]
    for a in A:
        counts[a] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    sorted_A = [0 for _ in range(len(A))]
    for i in range(len(A) - 1, -1, -1):
        sorted_A[counts[A[i]] - 1] = A[i]
        counts[A[i]] -= 1
    return sorted_A


def allocation():
    T = int(input())
    for x in range(1, T + 1):
        N, B = list(map(int, input().split()))
        A = list(map(int, input().split()))
        A = counting_sort(A)
        res, sum = 0, 0
        for a in A:
            sum += a
            if sum > B:
                break
            res += 1
        print('Case #{}: {}'.format(x, res))


if __name__ == '__main__':
    allocation()
