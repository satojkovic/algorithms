import itertools


def tower(perm, blocks):
    ret = []
    for p in perm:
        ret.append(blocks[p])
    return ''.join(ret)


def check(s):
    chars = set(s)
    grouped_s = [k for k, g in itertools.groupby(s)]
    return len(chars) == len(grouped_s)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    blocks = input().split()
    perms = itertools.permutations(range(N), N)
    ret = False
    for perm in perms:
        s = tower(perm, blocks)
        if check(s):
            print('Case #{}: {}'.format(t, s))
            ret = True
            break
    if not ret:
        print('Case #{}: {}'.format(t, 'IMPOSSIBLE'))
