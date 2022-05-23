def check(s):
    import string
    cond = {'has_lower': False, 'has_upper': False, 'has_digits': False, 'has_special': False}
    ascii_special = ['*', '&', '@', '#']
    for c in s:
        if c in string.ascii_lowercase:
            cond['has_lower'] = True
        elif c in string.ascii_uppercase:
            cond['has_upper'] = True
        elif c in string.digits:
            cond['has_digits'] = True
        elif c in ascii_special:
            cond['has_special'] = True
    return cond


def gen(s, cond):
    s_ex = []
    if not cond['has_lower']:
        s_ex.append('a')
    if not cond['has_upper']:
        s_ex.append('A')
    if not cond['has_digits']:
        s_ex.append('0')
    if not cond['has_special']:
        s_ex.append('*')
    return ''.join([s, ''.join(s_ex)])


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    s = input().rstrip()
    cond = check(s)
    new_passwd = gen(s, cond)
    if len(new_passwd) < 7:
        s_ex = []
        for _ in range(7 - len(new_passwd)):
            s_ex.append('a')
        new_passwd = ''.join([new_passwd, ''.join(s_ex)])
    print('Case #{}: {}'.format(t, new_passwd))
