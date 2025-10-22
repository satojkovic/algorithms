def permutations(nums):
    if len(nums) == 1:
        return [nums]
    res = []
    for i, n in enumerate(nums):
        former, latter = nums[:i], nums[i + 1 :]
        perms = permutations(former + latter)
        for p in perms:
            res.append(p + [n])
    return res


def perm_backtrack(nums):
    def backtrack(curr):
        if len(curr) == len(nums):
            res.append(curr[:])  # curr[:] means copy values
            return
        for i in range(len(nums)):
            if not seen[i]:
                curr.append(nums[i])
                seen[i] = True
                backtrack(curr)
                seen[i] = False
                curr.pop()

    res = []
    seen = [False] * len(nums)
    backtrack([])
    return res

def perm1(nums):
    if len(nums) < 2:
        return [nums]
    ret = []
    for i, num in enumerate(nums):
        pivot = num
        perm = perm1(nums[:i] + nums[i + 1 :])
        ret += [[pivot] + p for p in perm]
    return ret


def perm2(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [[s]]
    ret = []
    for i, ch in enumerate(s):
        res = perm2(s[:i] + s[i + 1 :])
        ret.extend([[ch] + r for r in res])
    return ret


def perm3(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [[s]]
    ret = []
    for c in s:
        [ret.append([c] + p) for p in perm3(s.replace(c, ""))]
    return ret


def perm4(s):
    from collections import Counter

    chars_counter = Counter(s)

    def _perm(chars_counter, prefix, remaining):
        if remaining == 0:
            return [prefix] if prefix != "" else []
        ret = []
        for c in chars_counter:
            count = chars_counter[c]
            if count > 0:
                chars_counter[c] -= 1
                ret.extend(_perm(chars_counter, prefix + c, remaining - 1))
                chars_counter[c] = count
        return ret

    return _perm(chars_counter, "", len(s))
