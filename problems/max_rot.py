def max_rot(A):
    A2 = A + A
    n = len(A)
    curr_sum = sum([i * A[i] for i in range(n)])
    res = curr_sum
    for i in range(n - 1, 0, -1):
        curr_sum = curr_sum - (n - 1) * A2[i] + sum(A2[i+1:i+n])
        res = curr_sum if res < curr_sum else res
    return res

if __name__ == '__main__':
    print(max_rot([4, 3, 2, 6]))
