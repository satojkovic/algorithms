from collections import defaultdict
def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    h = defaultdict(int)
    for ch in s1:
        h[ch] += 1
    for ch in s2:
        if not ch in h:
            return False
        else:
            h[ch] -= 1
            if h[ch] < 0:
                return False
    return True

if __name__ == "__main__":
    print(check_permutation('dog', 'god'))
    print(check_permutation('Dog', 'god')) # Case sensitive
    print(check_permutation('aaa', 'aa'))