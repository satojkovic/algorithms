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

def gen_parens_bf(n):
    def _gen_parens_bf(n, curr):
        if n == 1:
            return [[curr]]
        res = []
        left = _gen_parens_bf(n - 1, '(')
        right = _gen_parens_bf(n - 1, ')')
        [res.append([curr] + l) for l in left]
        [res.append([curr] + r) for r in right]
        return res

    def _valid(paren):
        v = 0
        for p in paren:
            if p == '(':
                v += 1
            elif p == ')':
                v -= 1
            if v < 0:
                return False
        return v == 0

    ans = []
    parens = _gen_parens_bf(n*2, '(')
    for paren in parens:
        if _valid(paren):
            ans.append(paren)
    return [''.join(a) for a in ans]
