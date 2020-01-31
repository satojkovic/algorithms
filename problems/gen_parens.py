def gen_parens(n):
    if n == 0:
        return []
    if n == 1:
        return ['()']
    res = []
    for p in gen_parens(n - 1):
        res.append('()' + p)
        res.append(p + '()')
        res.append('(' + p + ')')
        for i in [i for i, x in enumerate(p) if p[i] == '(']:
            res.append(p[:i+1] + '()' + p[i+1:])
    return list(set(res))