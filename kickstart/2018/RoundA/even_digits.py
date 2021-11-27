def is_even_digits(n):
    sn = str(n)
    return all([True if int(c) % 2 == 0 else False for c in sn])


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cx = 0
    for i, n in enumerate(range(N, -1, -1)):
        if is_even_digits(n):
            cx = i
            break
    n = N + 1
    cy = 1
    while n < 10 ** 16:
        if is_even_digits(n):
            break
        cy += 1
        n += 1
    print('Case #{}: {}'.format(t, min(cx, cy)))
