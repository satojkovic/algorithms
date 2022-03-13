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
        for m in range(N):
            if S[m] == "C" and m == 0:
                dp["C"] = 0
                # Heavily penalise attempt to change hardwired C to J
                dp["J"] = INF
            if S[m] == "J" and m == 0:
                # Heavily penalise attempt to change hardwired J to C
                dp["C"] = INF
                dp["J"] = 0
            if S[m] == "?" and m == 0:
                dp["C"] = 0
                dp["J"] = 0

            if S[m] == "C" and m > 0 and S[m-1] == "C":
                dp["C"] = prev_dp["C"]
                dp["J"] = INF
            if S[m] == "C" and m > 0 and S[m-1] == "J":
                dp["C"] = prev_dp["J"]+costJC
                dp["J"] = INF
            if S[m] == "J" and m > 0 and S[m-1] == "C":
                dp["C"] = INF
                dp["J"] = prev_dp["C"]+costCJ
            if S[m] == "J" and m > 0 and S[m-1] == "J":
                dp["C"] = INF
                dp["J"] = prev_dp["J"]

            if S[m] == "?" and m > 0 and S[m-1] == "C":
                dp["C"] = prev_dp["C"]
                dp["J"] = prev_dp["C"]+costCJ
            if S[m] == "?" and m > 0 and S[m-1] == "J":
                dp["C"] = prev_dp["J"]+costJC
                dp["J"] = prev_dp["J"]

            if S[m] == "C" and m > 0 and S[m-1] == "?":
                dp["C"] = min(prev_dp["C"], prev_dp["J"]+costJC)
                dp["J"] = INF
            if S[m] == "J" and m > 0 and S[m-1] == "?":
                dp["C"] = INF
                dp["J"] = min(prev_dp["C"]+costCJ, prev_dp["J"])
            if S[m] == "?" and m > 0 and S[m-1] == "?":
                dp["C"] = min(prev_dp["C"], prev_dp["J"]+costJC)
                dp["J"] = min(prev_dp["C"]+costCJ, prev_dp["J"])

            prev_dp["C"], prev_dp["J"] = dp["C"], dp["J"]
        print('Case #{}: {}'.format(t, min(dp["C"], dp["J"])))


if __name__ == '__main__':
    moons_and_umbrellas_dp()
