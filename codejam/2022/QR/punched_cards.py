def draw(r, c):
    if r <= 1 and c <= 1:
        return '.'
    elif r % 2 == 0 and c % 2 == 0:
        return '+'
    elif r % 2 != 0 and c % 2 == 0:
        return '|'
    elif r % 2 == 0 and c % 2 != 0:
        return '-'
    else:
        return '.'


T = int(input())
for t in range(1, T + 1):
    R, C = list(map(int, input().split()))
    ret = [[''] * (2*C + 1) for _ in range(2*R+1)]
    for r in range(2*R+1):
        for c in range(2*C+1):
            ret[r][c] = draw(r, c)
    print('Case #{}:'.format(t))
    for r in range(2*R+1):
        print(''.join(ret[r]))
