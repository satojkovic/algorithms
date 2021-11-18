import string


def append_letter(candidates, first_k_letters, N, count):
    next_candidates = []
    for c in first_k_letters:
        for cand in candidates:
            next_candidates.append(''.join([c, cand]))
    return next_candidates


def check_palindrome(candidates):
    res = 0
    for cand in candidates:
        i = 0
        j = len(cand) - 1
        while i < j:
            if cand[i] != cand[j]:
                break
            i += 1
            j -= 1
        res = res + 1 if i >= j else res
    return res


T = int(input())
letters = string.ascii_lowercase
for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    S = input()
    count = 0
    for i, c in enumerate(reversed(S)):
        count += letters.index(c) * (K ** i)
    first_k_letters = letters[:K]
    candidates = [c for c in first_k_letters]
    for i in range(N - 1):
        candidates = append_letter(candidates, first_k_letters, N, count)
    candidates = candidates[:count]
    res = check_palindrome(candidates)
    print('Case #{}: {}'.format(t, res))
