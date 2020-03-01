# Time complexity: O(n)
# Space complexity: O(1)
def reverse_string(s):
    lo = 0
    hi = len(s) - 1
    while lo < hi:
        s[lo], s[hi] = s[hi], s[lo]
        lo += 1
        hi -= 1
    return s

def reverse_string_r(s):
    def _reverse(s, lo, hi):
        if hi <= lo:
            return s

        s[lo], s[hi] = s[hi], s[lo]
        return _reverse(s, lo + 1, hi - 1)
    return _reverse(s, 0, len(s) - 1)
