def plates(stack, i, num_used, N, P, K):
    # Brute force: O(K^N)
    if i >= N:
        return -1
    current_total = -1
    for n in range(K + 1):
        if num_used + n > P:
            break
        elif num_used + n == P:
            current_total = max(current_total, sum(stack[i][:n]))
        else:
            ret = plates(stack, i + 1, num_used + n, N, P, K)
            ret = ret + sum(stack[i][:n]) if ret != -1 else ret
            current_total = max(current_total, ret)
    return current_total

if __name__ == '__main__':
    stack = [[10, 10, 100, 30], [80, 50, 10, 50]]
    N = len(stack)
    K = len(stack[0])
    P = 5
    print(plates(stack, 0, 0, N, P, K))

    stack = [[80, 80], [15, 50], [20, 10]]
    N = len(stack)
    K = len(stack[0])
    P = 3
    print(plates(stack, 0, 0, N, P, K))
