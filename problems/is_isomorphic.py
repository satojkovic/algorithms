def is_isomorphic(s, t):
    m = {}
    inv_m = {}
    for i in range(len(s)):
        if s[i] in m and m[s[i]] != t[i]:
            return False
        if t[i] in inv_m and inv_m[t[i]] != s[i]:
            return False
        m[s[i]] = t[i]
        inv_m[t[i]] = s[i]
    return True