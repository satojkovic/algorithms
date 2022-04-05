import numpy as np


def calc_amount(min_inks):
    min_inks = np.array(min_inks)
    indexes = np.argsort(-min_inks)
    total = 0
    ret = [0, 0, 0, 0]
    for ind in indexes:
        amount = min_inks[ind]
        if total + amount >= 10 ** 6:
            ret[ind] = 10 ** 6 - total
            break
        ret[ind] = amount
        total += amount
    return ret


T = int(input())
for t in range(1, T + 1):
    inks = [list(map(int, input().split())) for _ in range(3)]
    inks = np.array(inks)
    min_inks = [min(inks[:, i]) for i in range(4)]
    if sum(min_inks) < 10 ** 6:
        print('Case #{}: IMPOSSIBLE'.format(t))
    else:
        ret = calc_amount(min_inks)
        print('Case #{}: {}'.format(t, ' '.join(list(map(str, ret)))))
