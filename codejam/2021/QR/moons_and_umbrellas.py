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
        dp = [0] * 2
        prev_dp = [0] * 2
        for m in range(N):
            if S[m] == "C" and m == 0:
                dp[0] = 0
                # Heavily penalise attempt to change hardwired C to J
                dp[1] = INF
            if S[m] == "J" and m == 0:
                # Heavily penalise attempt to change hardwired J to C
                dp[0] = INF
                dp[1] = 0
            if S[m] == "?" and m == 0:
                dp[0] = 0
                dp[1] = 0

            if S[m] == "C" and m > 0 and S[m-1] == "C":
                dp[0] = prev_dp[0]
                dp[1] = INF
            if S[m] == "C" and m > 0 and S[m-1] == "J":
                dp[0] = prev_dp[1]+costJC
                dp[1] = INF
            if S[m] == "J" and m > 0 and S[m-1] == "C":
                dp[0] = INF
                dp[1] = prev_dp[0]+costCJ
            if S[m] == "J" and m > 0 and S[m-1] == "J":
                dp[0] = INF
                dp[1] = prev_dp[1]

            if S[m] == "?" and m > 0 and S[m-1] == "C":
                dp[0] = prev_dp[0]
                dp[1] = prev_dp[0]+costCJ
            if S[m] == "?" and m > 0 and S[m-1] == "J":
                dp[0] = prev_dp[1]+costJC
                dp[1] = prev_dp[1]

            if S[m] == "C" and m > 0 and S[m-1] == "?":
                dp[0] = min(prev_dp[0], prev_dp[1]+costJC)
                dp[1] = INF
            if S[m] == "J" and m > 0 and S[m-1] == "?":
                dp[0] = INF
                dp[1] = min(prev_dp[0]+costCJ, prev_dp[1])
            if S[m] == "?" and m > 0 and S[m-1] == "?":
                dp[0] = min(prev_dp[0], prev_dp[1]+costJC)
                dp[1] = min(prev_dp[0]+costCJ, prev_dp[1])

            prev_dp[0], prev_dp[1] = dp[0], dp[1]
        print('Case #{}: {}'.format(t, min(dp[0], dp[1])))


if __name__ == '__main__':
    moons_and_umbrellas_dp()
