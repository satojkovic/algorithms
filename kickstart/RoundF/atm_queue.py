import math
import numpy as np

def atm_queue(N, X, amounts):
    counts = []
    for i, a in enumerate(amounts):
        counts.append(math.ceil(a / X))
    res = sorted(range(len(counts)), 
            key=lambda k: counts[k])
    print('Case #: {}'.format(
        ' '.join(list(map(str, [r + 1 for r in res])))))

if __name__ == '__main__':
    N, X = 5, 6
    amounts = [9, 10, 4, 7, 2]
    atm_queue(N, X, amounts)
