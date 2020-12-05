def atoi(s) -> int:
    s = s.strip()
    if len(s) == 0:
        return 0
    sign = -1 if s[0] == '-' else 1
    i = 1 if s[0] in ['-','+'] else 0
    ret = 0
    while i < len(s) and s[i].isdigit():
        ret = ret*10 + ord(s[i]) - ord('0')
        i += 1
    return max(-2**31, min(sign * ret,2**31-1))