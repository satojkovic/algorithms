def max_rot(A):
    A2 = A + A
    n = len(A)
    cum_sum = [0 for _ in range(len(A2))]
    for i in range(len(A2)):
        cum_sum[i] = cum_sum[i-1] + A2[i] if i != 0 else A2[i]
    curr_sum = sum([i * A[i] for i in range(n)])
    res = curr_sum
    for i in range(n - 1, 0, -1):
        curr_sum = curr_sum - (n - 1) * A2[i] + cum_sum[i+n-1] - cum_sum[i]
        res = curr_sum if res < curr_sum else res
    return res

if __name__ == '__main__':
    print(max_rot([4, 3, 2, 6]))
