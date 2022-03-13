def moons_and_umbrellas():
    def calc_cost(sa, sb, X, Y):
        if sa + sb == 'CJ':
            return X
        elif sa + sb == 'JC':
            return Y
        else:
            return 0

    T = int(input())
    for t in range(1, T + 1):
        X, Y, S = input().split()
        X, Y = int(X), int(Y)
        N = len(S)
        cost, i, stack = 0, 0, []
        for i in range(N):
            if S[i] != '?':
                cost = cost + \
                    calc_cost(stack[-1], S[i], X, Y) if len(stack) != 0 else 0
                stack.append(S[i])
            else:
                if len(stack) != 0:
                    stack.append(stack[-1])
        print('Case #{}: {}'.format(t, cost))


def moons_and_umbrellas_dp():
    INF = float('inf')
    T = int(input())
    for t in range(1, T + 1):
        X, Y, S = input().split()
        costCJ, costJC = int(X), int(Y)
        N = len(S)
        dp = {k: 0 for k in ["C", "J"]}
        prev_dp = {k: 0 for k in ["C", "J"]}
        costs = {"C": costCJ, "J": costJC}
        for m in range(N):
            for i, j in [("C", "J"), ("J", "C")]:
                if S[m] == i and m == 0:
                    dp[i] = 0
                    dp[j] = INF

                if S[m] == i and m > 0 and S[m-1] == i:
                    dp[i] = prev_dp[i]
                    dp[j] = INF
                if S[m] == i and m > 0 and S[m-1] == j:
                    dp[i] = prev_dp[j]+costs[j]
                    dp[j] = INF

                if S[m] == "?" and m > 0 and S[m-1] == i:
                    dp[i] = prev_dp[i]
                    dp[j] = prev_dp[i]+costs[i]

                if S[m] == i and m > 0 and S[m-1] == "?":
                    dp[i] = min(prev_dp[i], prev_dp[j]+costs[j])
                    dp[j] = INF
                if S[m] == "?" and m > 0 and S[m-1] == "?":
                    dp[i] = min(prev_dp[i], prev_dp[j]+costs[j])

            prev_dp["C"], prev_dp["J"] = dp["C"], dp["J"]
        print('Case #{}: {}'.format(t, min(dp["C"], dp["J"])))


if __name__ == '__main__':
    moons_and_umbrellas_dp()
