def bulb_switch(n):
    bulbs = [1 for _ in range(n)]
    for i in range(1, n + 1):
        if i == 1:
            continue
        elif i == n:
            bulbs[-1] = 0 if bulbs[-1] == 1 else 1
        else:
            for j in range(i - 1, n, i):
                bulbs[j] = 0 if bulbs[j] == 1 else 1
    return sum(bulbs)