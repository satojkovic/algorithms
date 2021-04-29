def gen_groups(words, i):
    if i == len(words) - 1:
        return [[[words[i]]]]

    res = []
    groups = gen_groups(words, i + 1)
    for group in groups:
        for k, elem in enumerate(group):
            new_elem = elem + [words[i]]
            new_group = [new_elem]
            if k != 0:
                new_group.extend(group[:k])
            if k < len(group) - 1:
                new_group.extend(group[k+1:])
            res.append(new_group)
        group.append([words[i]])
        res.append(group)
    return res


class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.count = 0


def insert(root, s):
    curr = root
    for c in s:
        idx = ord(c) - ord('A')
        if curr.child[idx] is None:
            curr.child[idx] = TrieNode()
        curr = curr.child[idx]
    curr.count += 1


def calc_score(root, depth, K):
    curr_score, curr_count = 0, 0
    for i in range(26):
        if root.child[i] is not None:
            score, count = calc_score(root.child[i], depth + 1, K)
            curr_score += score
            curr_count += count
    curr_count += root.count
    while curr_count >= K:
        curr_count -= K
        curr_score += depth
    return curr_score, curr_count


def bundling():
    T = int(input())
    for t in range(1, T + 1):
        N, K = list(map(int, input().split()))
        strings = []
        for i in range(N):
            strings.append(input())

        root = TrieNode()
        for s in strings:
            insert(root, s)

        score, _ = calc_score(root, 0, K)
        print('Case #{}: {}'.format(t, score))


if __name__ == '__main__':
    bundling()
