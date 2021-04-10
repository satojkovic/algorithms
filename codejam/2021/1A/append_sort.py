def count_digits(X):
    if X == 0:
        return 0
    return count_digits(X//10) + 1


def append_sort():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        Xs = list(map(int, input().split()))
        res = 0
        for i in range(1, N):
            next_val = Xs[i - 1] + 1
            if next_val < Xs[i]:
                continue
            digits_curr = count_digits(Xs[i])
            digits_prev = count_digits(next_val)
            prefix_prev = int(str(next_val)[:digits_curr])
            if prefix_prev < Xs[i]:
                ops = abs(digits_curr - digits_prev)
                val = int(str(Xs[i]) + '0' * ops)
            elif prefix_prev > Xs[i]:
                ops = abs(digits_curr - digits_prev) + 1
                val = int(str(Xs[i]) + '0' * ops)
            elif prefix_prev == Xs[i]:
                ops = abs(digits_curr - digits_prev)
                val = next_val
            Xs[i] = val
            res += ops
        print('Case #{}: {}'.format(t, res))


if __name__ == '__main__':
    append_sort()
