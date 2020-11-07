def triple_steps_brute_force(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return triple_steps_brute_force(n - 1) + triple_steps_brute_force(n - 2) + triple_steps_brute_force(n - 3)

def triple_steps(n):
    def steps(n, memo):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif memo[n]:
            return memo[n]
        else:
            memo[n] = steps(n - 1, memo) + steps(n - 2, memo) + steps(n - 3, memo)
            return memo[n]
    memo = [0 for _ in range(n + 1)]
    return steps(n, memo)

if __name__ == "__main__":
    print(triple_steps_brute_force(5))
    print(triple_steps(5))