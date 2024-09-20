def gcd_string(str1, str2):
    def is_gcd_string(k):
        if len(str1) % k or len(str2) % k:
            return False
        n1, n2 = len(str1) // k, len(str2) // k
        prefix = str1[:k]
        return str1 == prefix * n1 and str2 == prefix * n2

    for i in range(min(len(str1), len(str2)), 0, -1):
        if is_gcd_string(i):
            return str1[:i]
    return ""