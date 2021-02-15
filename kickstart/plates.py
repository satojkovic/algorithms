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

def cumulative_sum(stack, N, K):
    cum_sum = []
    for i in range(N):
        cum_sum_i = [0 for _ in range(K + 1)]
        for j in range(K):
            cum_sum_i[j + 1] = cum_sum_i[j] + stack[i][j]
        cum_sum.append(cum_sum_i)
    return cum_sum

def plates_dp(stack, N, P, K):
    dp = [[0] * (P + 1) for _ in range(N + 1)]
    cum_sum = cumulative_sum(stack, N, K)
    for i in range(1, N + 1):
        for j in range(0, P + 1):
            dp[i][j] = 0
            for x in range(min(j, K) + 1):
                dp[i][j] = max(dp[i][j], cum_sum[i - 1][x] + dp[i - 1][j - x])
    return dp[N][P]

if __name__ == '__main__':
    stack = [[10, 10, 100, 30], [80, 50, 10, 50]]
    N = len(stack)
    K = len(stack[0])
    P = 5
    print(plates(stack, 0, 0, N, P, K))
    print(plates_dp(stack, N, P, K))

    stack = [[80, 80], [15, 50], [20, 10]]
    N = len(stack)
    K = len(stack[0])
    P = 3
    print(plates(stack, 0, 0, N, P, K))
    print(plates_dp(stack, N, P, K))
