import re

def gen_parens(n):
    if n == 1:
        return ['()']
    res = []
    for p in gen_parens(n - 1):
        for i in [m.start() for m in re.finditer(r'\(', p)]:
            res.append(''.join([p[:i+1] + '()' + p[i+1:]]))
        res.append(''.join(['()', p]))
    return list(set(res))

def gen_parens2(n):
    def parens(n, n_left, n_right, s, pos):
        if n_left < 0 or n_left > n_right:
            return
        if n_left == 0 and n_right == 0:
            return [''.join(s)] if len(s) != 0 else []
        ret = []
        if n_left > 0:
            s[pos] = '('
            res = parens(n, n_left - 1, n_right, s, pos + 1)
            ret.extend(res)
        if n_left < n_right:
            s[pos] = ')'
            res = parens(n, n_left, n_right - 1, s, pos + 1)
            ret.extend(res)
        return ret
    return parens(n, n, n, [''] * (2 * n), 0)

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

def gen_parens_bt(n):
    def _gen_parens_bt(N, n, curr, l, r):
        if l < r or N // 2 < l:
            return None
        if n == 1:
            return [[curr]] if l + r == N else None
        res = []
        left = _gen_parens_bt(N, n - 1, '(', l + 1, r)
        right = _gen_parens_bt(N, n - 1, ')', l, r + 1)
        if left:
            [res.append([curr] + l) for l in left]
        if right:
            [res.append([curr] + r) for r in right]
        return res
    ans = _gen_parens_bt(n * 2, n * 2, '(', 1, 0)
    return [''.join(a) for a in ans]