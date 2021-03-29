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
                cost = cost + calc_cost(stack[-1], S[i], X, Y) if len(stack) != 0 else 0
                stack.append(S[i])
            else:
                if len(stack) != 0:
                    stack.append(stack[-1])
        print('Case #{}: {}'.format(t, cost))

if __name__ == '__main__':
    moons_and_umbrellas()
