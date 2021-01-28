def min_copy_pastes(n):
    dp = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        dp[i] = i
        for j in range(i - 1, 1, -1):
            if i % j == 0:
                dp[i] = dp[j] + (i // j)
                break
    return dp[n]

if __name__ == "__main__":
    print('min_copy_pastes({}) => {}'.format(5, min_copy_pastes(5)))
    print('min_copy_pastes({}) => {}'.format(6, min_copy_pastes(6)))